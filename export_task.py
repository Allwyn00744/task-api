import pandas as pd
from database import SessionLocal
from models import TaskModel

db=SessionLocal()

tasks=db.query(TaskModel).all()

data=[]

for task in tasks:
    data.append({
        "title":task.title,
        "priority":task.final_priority
    })

df=pd.DataFrame(data)

df.to_csv("retrain_dataset.csv",index=False)

print("Exported successfully")

