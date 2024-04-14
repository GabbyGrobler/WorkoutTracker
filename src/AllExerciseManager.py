from src.SingleExerciseManager import SingleExerciseManager

class AllExerciseManager:
    def __init__(self) -> None:
        self.exercises: dict[str, SingleExerciseManager] = {}

    def __str__(self):
        return f"AllExerciseManager: {{Exercises: {{{', '.join(f"{name}: {manager}" for name, manager in self.exercises.items())}}}}}"
