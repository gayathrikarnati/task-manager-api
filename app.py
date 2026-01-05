from fastapi import FastAPI
from models import create_table, add_task, get_tasks, delete_task

app = FastAPI()

# Make sure table exists when app starts
create_table()

@app.get("/")
def home():
    return {"message": "Task API running"}

@app.post("/tasks")
def create_task(title: str):
    add_task(title)
    return {"status": "Task added", "title": title}

@app.get("/tasks")
def list_tasks():
    return get_tasks()

@app.delete("/tasks/{task_id}")
def remove_task(task_id: int):
    delete_task(task_id)
    return {"status": "Task deleted", "task_id": task_id}

