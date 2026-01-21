from rag.fossilite_rag.views import prompt_rag_application
from langgraph.runtime import Runtime
from typing import TypedDict, Dict
from dataclasses import dataclass
from states.college_app_state import CollegeAppState as State

class Context(TypedDict):
    """Context parameters for the agent.

    Set these when creating assistants OR when invoking the graph.
    See: https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/
    """

    user_prompt: str

    


async def obtain_rag_async(state: State, runtime: Runtime[Context]) -> Dict[str, str]:
    return await prompt_rag_application(state.user_application_info)




#testing purposes only
# if __name__ == "__main__":
#     print(obtain_rag("What is the capital of France?"))