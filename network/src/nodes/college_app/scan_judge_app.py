
from states.college_app_state import CollegeAppState as State
from typing import TypedDict, Dict
from langgraph.runtime import Runtime
from helper.obtain_rag import obtain_cds_rag_async




class Context(TypedDict):
    user_prompt: str



async def scan_judge_app_async(state: State, runtime: Runtime[Context]) -> Dict[str, str]:
    
    if state.user_application_info is None:
        return None


    #TODO: verify response from rag is valid
    rag_response = await obtain_cds_rag_async(state, runtime)

    #assume the response is valid for now
    score = rag_response.split()[0]
    feedback = rag_response.split()[1:]

    return (score, feedback)



    