"""Generate study plan node for SAT prep agent."""

from typing import Any, Dict

from langgraph.runtime import Runtime

from ..states.sat_prep_state import SATPrepState


async def generate_study_plan(state: SATPrepState, runtime: Runtime) -> Dict[str, Any]:
    """Generates a personalized study plan based on analysis.
    
    Args:
        state: Current SAT prep state
        runtime: LangGraph runtime
        
    Returns:
        Dictionary with personalized study plan
    """
    focus_areas = state.get_study_focus_areas()
    current_score = (
        state.get_previous_scores()[-1] 
        if state.get_previous_scores() 
        else (0, 0)
    )

    study_plan = {
        "student_name": state.get_student_name(),
        "current_level": current_score,
        "target_score": state.get_target_score(),
        "weak_areas": state.get_weak_areas(),
        "recommended_practice_questions": state.practice_questions or [],
        "gaps": {
            "math": focus_areas.get("math_gap", 0),
            "english": focus_areas.get("english_gap", 0)
        },
        "study_recommendation": _generate_recommendation(focus_areas, state.get_weak_areas())
    }

    return study_plan


def _generate_recommendation(focus_areas: dict, weak_areas: list[str]) -> str:
    """Generates a text recommendation based on focus areas."""
    recommendations = []
    
    if focus_areas.get("math_gap", 0) > 0:
        recommendations.append(f"Focus on math - gap of {focus_areas['math_gap']} points")
    
    if focus_areas.get("english_gap", 0) > 0:
        recommendations.append(f"Focus on English - gap of {focus_areas['english_gap']} points")
    
    if not recommendations:
        return "You're on track to meet your target score!"
    
    return " | ".join(recommendations)
