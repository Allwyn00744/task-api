from fastapi import APIRouter,Header,HTTPException
from schemas import Task,UpdateTask

router = APIRouter()

tasks=[]
task_counter=1

#create task
@router.post("/tasks")
def create_task(task:Task):
    global task_counter
    new_task={
        "id":task_counter,
        "title":task.title,
        "description":task.description,
        "priority":task.priority,
        "is_deleted":False
    }

    tasks.append(new_task)
    task_counter+=1

    return new_task

#Get all tasks
@router.get("/tasks")
def get_tasks(
    priority:str=None,
    x_user_name:str=Header(None)
):
    filtered_tasks=[t for t in tasks if not  t["is_deleted"]]
    if priority is not  None:
        filtered_tasks = [
    t for t in tasks 
    if not t["is_deleted"] and t["priority"] == priority
    ]
    return {
        "user":x_user_name,
        "tasks":filtered_tasks
    }
#get single task
@router.get("/tasks/{task_id}")
def get_task(task_id:int):
    for task in tasks:
        if task["id"]==task_id and not task["is_deleted"]:
            return task
    raise HTTPException(status_code=404,detail="Task not found")
        
    
@router.put("/tasks/{task_id}")
def update_task(task_id:int,updated:UpdateTask):
    for task in tasks:
        if task["id"]==task_id and not task["is_deleted"]:
            if updated.description is not None:
                task["description"]=updated.description
            if updated.priority is not None:
                task["priority"]=updated.priority
            return {"message":"Task Updated","task":task}
    raise HTTPException(status_code=404,detail="Task not found")

@router.delete("/tasks/{task_id}")
def delete_task(task_id:int):
    for task in tasks:
        if task["id"]==task_id and not task["is_deleted"]:
            task["is_deleted"]=True
            return {"message":"Task Deleted"}
    raise HTTPException(status_code=404,detail="Task not found")
    

