from states.college_app_state import CollegeAppState as State
from typing import TypedDict, Dict
from langgraph.runtime import Runtime

class Context(TypedDict):
    user_prompt: str


async def essay_review_async(state: State, runtime: Runtime[Context]) -> Dict[str, str]:
    return {
        "changeme": "output from essay_review. "
        f"Configured with {(runtime.context or {}).get('my_configurable_param')}"
    }