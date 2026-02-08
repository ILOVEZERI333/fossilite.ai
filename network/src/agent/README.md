# SAT Prep Agent Structure

This directory contains the SAT preparation agent organized into separate, reusable components.

## Directory Layout

```
agent/
├── states/
│   └── sat_prep_state.py          # State dataclass with all methods
├── nodes/
│   ├── __init__.py                # Node exports
│   ├── validate_input.py          # Input validation node
│   ├── analyze_performance.py     # Performance analysis node
│   └── generate_study_plan.py     # Study plan generation node
├── graphs/
│   └── sat_prep.py                # Graph assembly and connections
└── example_usage.py               # Usage example
```

## Components

### 1. **States** (`states/sat_prep_state.py`)
Contains the `SATPrepState` dataclass which:
- Holds all state data (student profile, scores, etc.)
- Includes validation methods
- Includes getter/analysis methods
- Includes update methods
- Is the single source of truth for data structure

**Why**: Centralized state definition makes it easy to modify data structure in one place.

### 2. **Nodes** (`nodes/`)
Individual async functions that process the state:
- **`validate_input.py`** - Validates student profile and initializes weak areas
- **`analyze_performance.py`** - Analyzes scores and identifies learning gaps
- **`generate_study_plan.py`** - Creates personalized recommendations

**Why**: Separating nodes makes each one:
- Easy to test independently
- Reusable in different graphs
- Focused on a single responsibility
- Easy to parallelize if needed

### 3. **Graph** (`graphs/sat_prep.py`)
Assembles nodes into a workflow:
- Creates StateGraph with SATPrepState
- Adds each node
- Defines edges (connections between nodes)
- Compiles the graph

**Why**: This is the orchestration layer that ties everything together.

## Workflow

```
START
  ↓
validate_input (Check profile, update weak areas)
  ↓
analyze_performance (Calculate gaps and improvement)
  ↓
generate_study_plan (Create recommendations)
  ↓
END
```

## Adding a New Node

1. Create `nodes/new_node.py`:
```python
from typing import Any, Dict
from langgraph.runtime import Runtime
from ..states.sat_prep_state import SATPrepState

async def my_new_node(state: SATPrepState, runtime: Runtime) -> Dict[str, Any]:
    """Node docstring."""
    # Process state
    return {"key": "value"}
```

2. Export in `nodes/__init__.py`:
```python
from .new_node import my_new_node
__all__ = ["my_new_node"]
```

3. Add to graph in `graphs/sat_prep.py`:
```python
.add_node("my_new_node", my_new_node)
.add_edge("previous_node", "my_new_node")
```

## Adding a New State Field

Just add it to `SATPrepState` in `states/sat_prep_state.py`:
```python
@dataclass
class SATPrepState:
    # ... existing fields ...
    new_field: Optional[str] = None
```

All nodes automatically have access to it!

## Running the Agent

```python
from src.agent.graphs.sat_prep import graph
from src.agent.states.sat_prep_state import SATPrepState
import asyncio

state = SATPrepState(student_profile={"name": "John", "grade": 11})
result = await graph.ainvoke(state)
```

## Benefits of This Structure

✅ **Modularity** - Each component has a single responsibility
✅ **Testability** - Test nodes and state independently
✅ **Reusability** - Use nodes in different graphs
✅ **Maintainability** - Easy to find and modify code
✅ **Scalability** - Easy to add new nodes or graph variants
✅ **Clarity** - Clear separation of concerns
