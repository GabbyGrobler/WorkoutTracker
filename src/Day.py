from datetime import datetime
from typing import List

from src.Exercise import Exercise

class Day:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.exercises: List[Exercise] = []
    
    def addExercise(self, exercise: Exercise):
        self.exercises.append(exercise)
        return True

    def removeExercise(self, name: str):
        for exercise in self.exercises:
            if exercise.name==name:
                self.exercises.remove(exercise)
                return True
        return False
            
    def completeExercise(self, name: str):
        for exercise in self.exercises:
            if exercise.name==name:
                exercise.completeExercise()
                return True
        return False

    def __str__(self) -> str:
        return f'Day: {self.__class__.__name__}, Name: {self.name}, Exercises: [{', '.join([str(exercise) for exercise in self.exercises])}]'
    