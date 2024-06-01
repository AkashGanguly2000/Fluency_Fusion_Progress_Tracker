from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List
from app.services.progress_service import ProgressService
from app.models.progress import Progress
from datetime import date

router = APIRouter()

progress_service = ProgressService()

class ProgressIn(BaseModel):
    userId: int
    gameScore: float
    learningDuration: float
    language: str
    completionPercentage: str
    assessmentMarks: float
    CourseStartDate: date

@router.post("/progress", response_model=Progress)
def create_progress(progress_in: ProgressIn):
    return progress_service.create_progress(progress_in)

@router.get("/progress/{userId}", response_model=List[Progress])
def get_user_progress(userId: int):
    return progress_service.get_user_progress(userId)
