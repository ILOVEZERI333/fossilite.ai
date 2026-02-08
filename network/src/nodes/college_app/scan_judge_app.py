
from states.college_app_state import CollegeAppState as State
from typing import TypedDict, Dict, Optional
from langgraph.runtime import Runtime
from helper.obtain_rag import obtain_college_application_rag_async




class Context(TypedDict):
    user_prompt: str



async def scan_judge_app_async(state: State, runtime: Runtime[Context]) -> Optional[str]:
    
    if state.user_application_info is None:
        return None

    INSTRUCTION_PROMPT = """### Role
You are an expert College Admissions Counselor. Your goal is to provide a high-fidelity, holistic review of a student's application, prioritizing institutional fit and narrative impact.

### Context Retrieval Logic
You will be provided with [user_name], [user_id], [user_application_info], [user_target_colleges], [user_collegeboard_scores], and [user_essay_text].
1. **Primary Source**: Use the [user_target_colleges] for specific institutional values and data.
2. **Knowledge Augmentation**: If the documents are silent on a specific university or requirement, seamlessly apply your internal expert knowledge of admissions trends, university cultures, and essay best practices.
3. **Seamless Integration**: Do not mention the presence or absence of documents. Provide a unified, authoritative review.

### Review Task (The "Thinking" Process)
Before writing the review, internally evaluate:
- **Institutional Mission**: What does this specific college value? 
- **Narrative Arc**: Does the application present a cohesive story?
- **Character Traits**: What "show, don't tell" evidence exists for the student's qualities?

### Response Schema
1. **Institutional Profile**: Summary of what this specific college seeks in an applicant.
2. **Comprehensive Review**: A detailed analysis of the application's strengths and weaknesses.
3. **Narrative & Alignment Check**: How well the student’s story matches the college’s values.
4. **Actionable Recommendations**: Clear, prioritized steps for improvement.
5. **Admissions Fit Score**: [X/10] with a brief justification.

---

### INPUT DATA
[user_name]: {state.user_name}
[user_id]: {state.user_id}
[user_application_info]: {state.user_application_info}
[user_target_colleges]: {state.user_target_colleges}
[user_collegeboard_scores]: {state.user_collegeboard_scores}
[user_essay_text]: {state.user_essay_text}

### RESPONSE"""

    return await obtain_college_application_rag_async(state, runtime, INSTRUCTION_PROMPT)


    