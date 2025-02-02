# Entry Point

from fastapi import FastAPI
from routes import tasks
from database import engine, Base

# Initialize Database
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(tasks.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Task Manager API"}