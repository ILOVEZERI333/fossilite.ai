"""LangGraph single-node graph template.

Returns a predefined response. Replace logic and configuration as needed.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional

from states.college_app_state import CollegeAppState as State
from langgraph.graph import StateGraph
from langgraph.runtime import Runtime
from typing_extensions import TypedDict
from nodes.college_app.help_apply import help_apply_async
from nodes.college_app.scan_judge_app import scan_judge_app_async
from nodes.college_app.value_review import values_check_async
from nodes.general.output_format import output_format_async
from nodes.general.output_check import output_check_async
from nodes.college_app.essay_review import essay_review_async
from rag.fossilite_rag.views import check_if_essay_required

class Context(TypedDict):
    """Context parameters for the agent.

    Set these when creating assistants OR when invoking the graph.
    See: https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/
    """

    model_name: str
    user_name: str

async def call_model(state: State, runtime: Runtime[Context]) -> Dict[str, Any]:
    """Process input and returns output.

    Can use runtime context to alter behavior.
    """
    return {
        "changeme": "output from call_model. "
        f"Configured with {(runtime.context or {}).get('my_configurable_param')}"
    }

"""
Conditional edges
"""

async def has_user_done_application(state: State) -> str:
    
    
    if not state.user_application_info:
        return "help_apply"
    return "scan_judge_application"

    messages: list
    user_personal_info: Optional[dict] = None

async def does_app_require_essay(state: State) -> str:
    
    #if user does not need essay help, avoid unnecessary node calls
    if state.user_application_info:

        #check if app requires essay
        essay_required = await check_if_essay_required(state.user_application_info) 


        if essay_required:
            return "essay_review"
        else:
            return "values_check"


    return "values_check"


#TODO: implement output validation via LLM call
async def is_output_valid(state: State) -> str:
    if state.output_valid:
        return "output_format"
    else:
        return "output_check"


# Define the graph
#TODO: help_apply, scan_judge_application (might be okay), values_check, output_format, output_check, essay_review
graph = (
    StateGraph(State, context_schema=Context)
    .add_node("output_format", output_format_async)
    .add_node("output_check", output_check_async)
    .add_node("scan_judge_application", scan_judge_app_async)
    .add_node("help_apply", help_apply_async)
    .add_conditional_edges("__start__", has_user_done_application)
    .add_node("values_check", values_check_async)
    .add_node("essay_review", essay_review_async)
    .add_conditional_edges("scan_judge_application", does_app_require_essay)
    .add_edge("values_search", "output_format")
    .add_edge("output_format", "output_check")
    .add_conditional_edges("output_check", is_output_valid)
    .compile(name="College Application Graph")
)

