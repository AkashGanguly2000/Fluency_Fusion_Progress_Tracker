from app.models.progress import Progress
from app.repositories.progress_repository import ProgressRepository
from datetime import date

class ProgressService:
    def __init__(self):
        self.progress_repo = ProgressRepository()

    def create_progress(self, progress_data):
        progress = Progress(
            id=len(self.progress_repo.progresses) + 1,
            userId=progress_data.userId,
            gameScore=progress_data.gameScore,
            learningDuration=progress_data.learningDuration,
            language=progress_data.language,
            completionPercentage=progress_data.completionPercentage,
            assessmentMarks=progress_data.assessmentMarks,
            CourseStartDate=progress_data.CourseStartDate,
        )
        return self.progress_repo.create(progress)

    def get_user_progress(self, userId: int):
        return self.progress_repo.get_by_user_id(userId)
