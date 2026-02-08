"""
Graph for the SAT preparation agent.

This module connects all the nodes and state to create the SAT prep agent workflow.
"""

from __future__ import annotations

from langgraph.graph import StateGraph

from ..states.sat_prep_state import SATPrepState
from ..nodes import (
    validate_input,
    analyze_performance,
    generate_study_plan
)


def create_sat_prep_graph():
    """Creates and compiles the SAT prep agent graph.
    
    The graph workflow:
    1. validate_input - Validates student profile and data
    2. analyze_performance - Analyzes scores and identifies gaps
    3. generate_study_plan - Creates personalized study plan
    
    Returns:
        Compiled LangGraph StateGraph
    """
    graph = (
        StateGraph(SATPrepState)
        .add_node("validate_input", validate_input)
        .add_node("analyze_performance", analyze_performance)
        .add_node("generate_study_plan", generate_study_plan)
        # Define edges for workflow
        .add_edge("__start__", "validate_input")
        .add_edge("validate_input", "analyze_performance")
        .add_edge("analyze_performance", "generate_study_plan")
        .add_edge("generate_study_plan", "__end__")
        .compile(name="SAT Prep Agent Graph")
    )
    
    return graph


# Create the graph instance
graph = create_sat_prep_graph()