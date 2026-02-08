from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class CollegeAppState:
    # rate limit retries
    retries: int = 0
    user_id: str = ""
    user_name: str = ""
    user_application_info: str = ""
    user_target_colleges: List[str] = []
    user_collegeboard_scores: Dict[str, int] = {}
    user_essay_text: Optional[str] = None