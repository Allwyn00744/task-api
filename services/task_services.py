from sqlalchemy.orm import Session
from models import TaskModel
from schemas import TaskCreate,TaskUpdate

def create_task_services(db:Session,Task:TaskCreate):
    new_Task=TaskModel(
        title=Task.title,
        description=Task.description,
        priority=Task.priority
    )
    db.add(new_Task)
    db.commit()
    db.refresh()
    return new_Task

def get_tasks_service(db: Session):
    tasks = db.query(TaskModel).filter(TaskModel.is_deleted == False).all()
    return tasks

def get_single_task_service(db: Session, task_id: int):
    task = db.query(TaskModel).filter(
        TaskModel.id == task_id,
        TaskModel.is_deleted == False
    ).first()

    return task

def update_task_service(db: Session, task_id: int, updated_task: TaskUpdate):
    task = db.query(TaskModel).filter(
        TaskModel.id == task_id,
        TaskModel.is_deleted == False
    ).first()

    if not task:
        return None

    if updated_task.description is not None:
        task.description = updated_task.description

    if updated_task.priority is not None:
        task.priority = updated_task.priority

    db.commit()
    db.refresh(task)

    return task

def delete_task_service(db: Session, task_id: int):
    task = db.query(TaskModel).filter(
        TaskModel.id == task_id,
        TaskModel.is_deleted == False
    ).first()

    if not task:
        return None

    task.is_deleted = True

    db.commit()

    return task