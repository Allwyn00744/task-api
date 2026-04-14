from sqlalchemy import Column,String,Integer,Boolean
from database import base

class TaskModel(base):
    __tablename__="tasks"
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String)
    description=Column(String)
    priority=Column(String)
    is_deleted=Column(Boolean,default=False)