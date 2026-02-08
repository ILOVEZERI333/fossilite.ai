"""Analyze performance node for SAT prep agent."""

from typing import Any, Dict

from langgraph.runtime import Runtime

from ..states.sat_prep_state import SATPrepState


async def analyze_performance(state: SATPrepState, runtime: Runtime) -> Dict[str, Any]:
    """Analyzes student performance based on scores and target.
    
    Args:
        state: Current SAT prep state
        runtime: LangGraph runtime
        
    Returns:
        Dictionary with performance analysis
    """
    improvement = state.calculate_score_improvement()
    focus_areas = state.get_study_focus_areas()
    current_score = (
        state.get_previous_scores()[-1] 
        if state.get_previous_scores() 
        else (0, 0)
    )

    analysis = {
        "current_score": current_score,
        "target_score": state.get_target_score(),
        "score_improvement": improvement,
        "study_focus": focus_areas,
        "weak_areas": state.get_weak_areas()
    }

    return analysis
