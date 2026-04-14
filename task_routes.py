from fastapi import HTTPException
from database import sessionLocal
from models import TaskModel

#Create task
@router.post("/tasks")
def create_task(task:Task):
    db=sessionLocal()
    new_task=TaskModel(
        title= task.title,
        description=task.description,
        priority=task.priority,
        is_deleted=False
        
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    db.close()
    
    return new_task

#Get all tasks
@router.get("/tasks")
def get_tasks():
    db=sessionLocal()
    tasks = db.query(TaskModel).filter(TaskModel.is_deleted == False).all()
    db.close()
    return tasks
#get single task
@router.get("/tasks/{task_id}")
def get_task(task_id:int):
    db=sessionLocal()

    task=db.query(TaskModel).filter(
        TaskModel.id==task_id,
        TaskModel.is_deleted==False
        ).first()
    db.close()

    if not task:
        raise HTTPException(status_code=404,detail="Task not found")
    return task  
#update   
@router.put("/tasks/{task_id}")
def update_task(task_id:int,updated:UpdateTask):
    db=sessionLocal()
    task=db.query(TaskModel).filter(TaskModel.id==task_id,TaskModel.is_deleted == False).first()
    if not  task:
        raise HTTPException(status_code=404,detail="Task not found")

    if updated.description is not None:
        task.description=updated.description
    if updated.priority is not None:
        task.priority=updated.priority
    db.commit()
    db.close()
    return {"message":"Task Updated"}
    
#delete task(soft delete)
@router.delete("/tasks/{task_id}")
def delete_task(task_id:int):
    db=sessionLocal()
    task=db.query(TaskModel).filter(TaskModel.id==task_id,TaskModel.is_deleted == False).first()
    
        
    
    if not task:
        raise HTTPException(status_code=404,detail="Task not found")

    task.is_deleted=True       
    
    db.commit()
    db.close()
    return {"message":"Task Deleted"}
    

