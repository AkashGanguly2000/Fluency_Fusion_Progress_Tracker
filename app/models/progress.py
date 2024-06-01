from pydantic import BaseModel
from datetime import date

class Progress(BaseModel):
    id: int
    userId: int
    gameScore: float
    learningDuration: float
    language: str
    completionPercentage: str
    assessmentMarks: float
    CourseStartDate: date

    class Config:
        orm_mode = True
