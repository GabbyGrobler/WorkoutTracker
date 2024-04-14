from typing import List
from src.Exercise import Exercise


class SingleExerciseManager:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.exercisesCompleted: List[Exercise] = []

    def addExercise(self, exercise: Exercise):
        self.exercisesCompleted.append(exercise)
        return True
    
    def __str__(self):
        return f"SingleExerciseManager: {{Name: {self.name}, Exercises Completed: [{', '.join(str(exercise) for exercise in self.exercisesCompleted)}]}}"
    