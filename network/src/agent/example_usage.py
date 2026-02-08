"""
Example usage of the SAT Prep Agent.

This demonstrates how to use the newly organized agent structure.
"""

import asyncio
from src.agent.graphs.sat_prep import graph
from src.agent.states.sat_prep_state import SATPrepState


async def main():
    """Example: Running the SAT prep agent."""
    
    # Create initial state
    state = SATPrepState(
        student_profile={
            "name": "John Doe",
            "grade": 11,
            "target_score": (1500, 1500)
        },
        practice_questions=["q1", "q2", "q3", "q4", "q5"],
        previous_scores=[(1200, 1150), (1250, 1200), (1300, 1250)],
        target_score=(1500, 1500),
        weak_areas=[]
    )
    
    # Run the agent
    print("Running SAT Prep Agent...")
    print("=" * 50)
    
    try:
        result = await graph.ainvoke(state)
        print("Agent Output:")
        print(result)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())
