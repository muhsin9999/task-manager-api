from fastapi import FastAPI

app = FastAPI(
    title="Task Manager API",
    description="A production-ready FastAPI backend for managing tasks.",
    version="0.1.0"
)

@app.get("/")
def root():
    return {"message": "Welcome to the Task Manager API!"}
