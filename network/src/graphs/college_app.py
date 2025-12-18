"""LangGraph single-node graph template.

Returns a predefined response. Replace logic and configuration as needed.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict

from states.college_app_state import CollegeAppState as State
from langgraph.graph import StateGraph
from langgraph.runtime import Runtime
from typing_extensions import TypedDict
from nodes.help_apply import help_apply_async


class Context(TypedDict):
    """Context parameters for the agent.

    Set these when creating assistants OR when invoking the graph.
    See: https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/
    """

    my_configurable_param: str



async def has_user_done_application(state: State) -> bool:
    
    
    if state.user_application_info is None:
        return False
    return True



# Define the graph
graph = (
    StateGraph(State, context_schema=Context)
    .add_node("help_apply", help_apply_async)
    .add_conditional_edges("__start__", has_user_done_application)
    .compile(name="New Graph")
)
