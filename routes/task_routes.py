from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from schemas import TaskCreate, TaskUpdate
from services.task_service import (
    create_task_services,
    get_tasks_service,
    get_single_task_service,
    update_task_service,
    delete_task_service
)
router =APIRouter()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


#Create task
@router.post("/tasks")
def create_task(task:TaskCreate,db:Session=Depends(get_db)):
    return create_task_services(db,task)

#Get all tasks
@router.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    return get_tasks_service(db)

#get single task
@router.get("/tasks/{task_id}")
def get_single_task(task_id: int, db: Session = Depends(get_db)):
    task = get_single_task_service(db, task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task

#update   
@router.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: TaskUpdate, db: Session = Depends(get_db)):
    task = update_task_service(db, task_id, updated_task)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task

#delete task(soft delete)
@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = delete_task_service(db, task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"message": "Task deleted successfully"}
    

