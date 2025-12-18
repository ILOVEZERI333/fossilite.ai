from rag.fossilite_rag.views import prompt_rag
from langgraph.runtime import Runtime
from typing import TypedDict, Dict
from dataclasses import dataclass

class Context(TypedDict):
    """Context parameters for the agent.

    Set these when creating assistants OR when invoking the graph.
    See: https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/
    """

    user_prompt: str

    


@dataclass
class State:
    """Input state for the agent.
    
    Defines the initial structure of incoming data.
    See: https://langchain-ai.github.io/langgraph/concepts/low_level/#state
    """

    prompt: str = ""
    rag_response: str = ""

async def obtain_rag_async(state: State, runtime: Runtime[Context]) -> Dict[str, str]:
    return await prompt_rag(state["prompt"])




#testing purposes only
# if __name__ == "__main__":
#     print(obtain_rag("What is the capital of France?"))