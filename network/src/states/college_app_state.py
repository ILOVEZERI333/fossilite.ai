from dataclasses import dataclass
from typing import Dict


@dataclass
class CollegeAppState:
    # rate limit retries
    retries: int = 0
    user_id: str = ""
    user_name: str = ""
    user_application_info: str = ""
    user_collegeboard_scores: Dict[str, int] = {}