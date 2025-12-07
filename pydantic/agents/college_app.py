import asyncio
from dataclasses import dataclass
from collections.abc import AsyncIterable
from datetime import date
from typing import Optional, List, Dict
import pypdf
import time


from pydantic_ai import (
    Agent,
    AgentStreamEvent,
    FinalResultEvent,
    FunctionToolCallEvent,
    FunctionToolResultEvent,
    PartDeltaEvent,
    PartStartEvent,
    RunContext,
    TextPartDelta,
    ThinkingPartDelta,
    ToolCallPartDelta,
)





@dataclass
class CollegeAppDeps:

    #user context
    user_id: str
    user_name: Optional[str] = None
    user_application_info: Optional[str] = None

    #api keys


    #external services
    

    #database connection



    #configuration


agent = Agent(
    model="gemini-2.5-flash",
    deps_type=CollegeAppDeps,
    instructions="You are a helpful assistant that can help with college applications.",
)


@agent.tool
def get_user_application_info(deps: CollegeAppDeps) -> str:
    pass

@agent.tool
def rag_search_college_essay() -> List[str]:
    return ["College essay 1", "College essay 2", "College essay 3", "College essay 4", "College essay 5"]

@agent.tool
def set_user_calendar_event(event_name: str, event_date: date, event_time: time) -> str:
    return f"Event {event_name} set for {event_date} at {event_time}"

@agent.tool
def google_search(query: str) -> List[str]:
    return ["Google search result 1", "Google search result 2", "Google search result 3", "Google search result 4", "Google search result 5"]

@agent.tool
def obtain_user_collegeboard_scores() -> Dict[str, int]:
    return {"SAT": 1500, "ACT": 30}
