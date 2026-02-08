"""Validate input node for SAT prep agent."""

from typing import Any, Dict

from langgraph.runtime import Runtime

from ..states.sat_prep_state import SATPrepState


async def validate_input(state: SATPrepState, runtime: Runtime) -> Dict[str, Any]:
    """Validates student profile and input data.
    
    Args:
        state: Current SAT prep state
        runtime: LangGraph runtime
        
    Returns:
        Dictionary with validated state fields
        
    Raises:
        ValueError: If student profile is invalid
    """
    if not state.validate_student_profile():
        raise ValueError(
            "Invalid student profile: missing required fields ['name', 'grade']"
        )

    # Update weak areas based on current scores
    state.update_weak_areas()

    return {
        "student_profile": state.student_profile,
        "practice_questions": state.practice_questions,
        "previous_scores": state.previous_scores,
        "target_score": state.target_score,
        "weak_areas": state.weak_areas
    }
