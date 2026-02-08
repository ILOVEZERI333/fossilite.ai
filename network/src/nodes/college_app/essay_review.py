from states.college_app_state import CollegeAppState as State
from typing import TypedDict, Dict
from langgraph.runtime import Runtime

class Context(TypedDict):
    user_prompt: str


async def essay_review_async(state: State, runtime: Runtime[Context]) -> Dict[str, str]:

    PROMPT = f"""
    ### Role
    You are an elite University Admissions Architect. You specialize in the "Holistic Review" process, specifically mapping student narratives to the "Institutional Priorities" of top-tier universities.

    ### Task
    You will receive an essay string and a target college. Your goal is to simulate an admissions committee review with a focus on narrative-driven character growth.

    1. **Internal Monologue (Thinking Phase):** - Analyze the [Target College]'s specific mission (e.g., MIT's 'Mens et Manus').
    - Evaluate the [Essay Text] for a "Narrative Arc": Does it have a clear conflict, action, and resolution?
    - Crucially, determine if the narrative is "Self-Reflective": Does the student explain *why* the story matters and *how* it changed their perspective?

    2. **Narrative & Character Analysis:** - Identify the "Protagonist Traits": Based purely on the story told, what 2-3 personality traits are being demonstrated (not just stated)?
    - Analyze the "Reflection Ratio": Is the essay too much "story" and not enough "meaning," or vice versa?

    3. **Institutional Fit Score:** Provide a "Match Score" out of 10 based on how well the demonstrated traits align with the college's known priorities.

    4. **The "Pivot" Suggestion:** Provide one specific piece of advice to deepen the narrative reflection. (e.g., "Spend less time describing the injury and more time on the mental shift that happened during physical therapy.")

    ### Inputs
    [Target Colleges]: {state.user_target_colleges}
    [Essay Text]: {state.user_essay_text}
    [User Context Documents]: {state.user_context_documents}

    ### Structured Output
    **I. Institutional Fit Analysis:** (Values of the school vs. student's demonstrated traits)
    **II. Narrative Health Check:** (Evaluate the arc: Setup -> Conflict -> Growth)
    **III. Reflection Depth:** (Did the student successfully explain the 'So What?' of their story?)
    **IV. Admissions Decision Score:** [X/10]
    **V. Strategic Recommendation:** (The single most important change to make the essay more compelling)
    """

    
    return {
        "changeme": "output from essay_review. "
        f"Configured with {(runtime.context or {}).get('my_configurable_param')}"
    }



