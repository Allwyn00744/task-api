from sqlalchemy.orm import Session
from models import TaskModel,UserModel
from schemas import TaskCreate,TaskUpdate
from services.ml_service import predict_priority


def create_task_services(db:Session,task:TaskCreate,current_user: UserModel):
    
    predicted=predict_priority(task.title).strip()
    user_priority=task.priority
    final_priority=user_priority if user_priority else predicted
    new_Task=TaskModel(
        title=task.title,
        description=task.description,
        user_priority=user_priority,
        predicted_priority=predicted,
        final_priority=final_priority,
        user_id=current_user.id
    )
    db.add(new_Task)
    db.commit()
    db.refresh(new_Task)
    return {
        "title":new_Task.title,
        "priority":new_Task.final_priority.strip()
    }

def get_tasks_service(db: Session,current_user: UserModel):
    tasks = db.query(TaskModel).filter(
        TaskModel.user_id==current_user.id,
        TaskModel.is_deleted == False).all()
    return tasks

def get_single_task_service(db: Session, task_id: int,current_user: UserModel):
    task = db.query(TaskModel).filter(
        TaskModel.id == task_id,
        TaskModel.user_id==current_user.id,
        TaskModel.is_deleted == False
    ).first()

    return task

def update_task_service(db: Session, task_id: int, updated_task: TaskUpdate,current_user: UserModel):
    task = db.query(TaskModel).filter(
        TaskModel.id == task_id,
        TaskModel.user_id==current_user.id,
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

def delete_task_service(db: Session, task_id: int,current_user: UserModel):
    task = db.query(TaskModel).filter(
        TaskModel.id == task_id,
        TaskModel.user_id==current_user.id,
        TaskModel.is_deleted == False
    ).first()

    if not task:
        return None

    task.is_deleted = True

    db.commit()

    return task