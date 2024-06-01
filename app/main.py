from fastapi import FastAPI
from app.controllers import progress_controller,health_controller

app = FastAPI(
    title='Fluency Fusion Progress Tracker',
    description='Fluency Fusion Progress Tracker features'
    )
app.include_router(progress_controller.router)
app.include_router(health_controller.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)
