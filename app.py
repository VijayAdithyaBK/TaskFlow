# Entry Point

from fastapi import FastAPI
from routes import task_router
from db import engine, Base

# Initialize Database
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(task_router.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Task Manager API"}