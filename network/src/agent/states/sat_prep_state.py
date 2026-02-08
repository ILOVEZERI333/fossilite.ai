from dataclasses import dataclass, field
from typing import Optional


@dataclass
class SATPrepState:
    """State for the SAT preparation agent.
    
    Defines the structure of data flowing through the agent.
    """
    
    student_profile: dict  # Keys: "name", "grade", "target_score"
    practice_questions: Optional[list[str]] = None
    previous_scores: Optional[list[tuple[int, int]]] = None  # (math, english)
    target_score: Optional[tuple[int, int]] = None  # (math_target, english_target)
    weak_areas: Optional[list[str]] = field(default_factory=list)

    # Validation methods
    def validate_student_profile(self) -> bool:
        """Validates that the student profile has required fields."""
        required_fields = ["name", "grade"]
        return all(field in self.student_profile for field in required_fields)

    def validate_practice_questions(self) -> bool:
        """Ensures practice questions are properly formatted."""
        if not self.practice_questions:
            return True
        return all(isinstance(q, str) for q in self.practice_questions)

    # Getter methods
    def get_student_name(self) -> str:
        """Retrieves the student's name."""
        return self.student_profile.get("name", "Unknown")

    def get_previous_scores(self) -> Optional[list[tuple[int, int]]]:
        """Retrieves previous test scores."""
        return self.previous_scores

    def get_target_score(self) -> Optional[tuple[int, int]]:
        """Retrieves target scores."""
        return self.target_score or self.student_profile.get("target_score")

    def get_weak_areas(self) -> list[str]:
        """Retrieves weak areas."""
        return self.weak_areas or []

    # Analysis methods
    def calculate_score_improvement(self) -> Optional[int]:
        """Calculates total score improvement."""
        if not self.previous_scores or len(self.previous_scores) < 2:
            return None
        first_score = self.previous_scores[0]
        last_score = self.previous_scores[-1]
        return (last_score[0] - first_score[0]) + (last_score[1] - first_score[1])

    def get_study_focus_areas(self) -> dict:
        """Determines focus areas based on gaps."""
        weak_areas = self.get_weak_areas()
        previous_score = self.get_previous_scores()[-1] if self.get_previous_scores() else (0, 0)
        target_score = self.get_target_score() or (1500, 1500)

        return {
            "focus_areas": weak_areas,
            "math_gap": target_score[0] - previous_score[0],
            "english_gap": target_score[1] - previous_score[1]
        }

    # Update methods
    def add_practice_score(self, score: tuple[int, int]) -> None:
        """Adds a new practice test score."""
        if self.previous_scores is None:
            self.previous_scores = []
        self.previous_scores.append(score)

    def update_weak_areas(self) -> None:
        """Updates weak areas based on latest scores."""
        if not self.previous_scores or not self.target_score:
            return

        if self.weak_areas is None:
            self.weak_areas = []

        latest_math, latest_english = self.previous_scores[-1]
        target_math, target_english = self.target_score

        if latest_math < target_math and "math" not in self.weak_areas:
            self.weak_areas.append("math")
        if latest_english < target_english and "english" not in self.weak_areas:
            self.weak_areas.append("english")

    # Data transformation
    def to_dict(self) -> dict:
        """Converts state to dictionary."""
        return {
            "student_profile": self.student_profile,
            "practice_questions": self.practice_questions,
            "previous_scores": self.previous_scores,
            "target_score": self.target_score,
            "weak_areas": self.weak_areas
        }