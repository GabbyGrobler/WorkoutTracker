from datetime import datetime

class Exercise:
    def __init__(self, name: str, weight: int, numberOfSets: int, numberOfReps: int) -> None:
        self.name: str = name
        self.weight: int = weight
        self.numberOfSets: int = numberOfSets
        self.numberOfReps: int = numberOfReps
        self.complete: bool = False
        self.timeCompleted: datetime = None
        
    def completeExercise(self):
        self.complete = True
        self.timeCompleted = datetime.now()

    def __str__(self) -> str:
        return (f'Exercise: {self.__class__.__name__}, '
                f'Name: {self.name}, '
                f'Weight: {self.weight}, '
                f'Number of Sets: {self.numberOfSets}, '
                f'Number of Reps: {self.numberOfReps}, '
                f'Complete: {self.complete}, '
                f'Time Completed: {self.timeCompleted}')