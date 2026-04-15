from sqlalchemy import Column,String,Integer,Boolean
from database import base

class TaskModel(base):
    __tablename__="tasks"
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String,nullable=False)
    description=Column(String,nullable=False)
    priority=Column(String,nullable=False)
    is_deleted=Column(Boolean,default=False)