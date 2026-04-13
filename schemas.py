from pydantic import BaseModel
from typing import Optional
class Task(BaseModel):
    title:str
    description:Optional[str]=None
    priority:str
class UpdateTask(BaseModel):
    description:Optional[str]=None
    priority:Optional[str]=None