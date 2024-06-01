from fastapi import APIRouter

router=APIRouter()

@router.get('/health')
def check_health():
    return "Fluency Fusion progress tracking service is running."
