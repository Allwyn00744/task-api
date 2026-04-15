from pydantic import BaseModel,Field
from typing import Optional
class TaskCreate(BaseModel):
    title:str=Field(...,min_length=3,max_length=100)
    description:Optional[str]=Field(None,max_length=300)
    priority:str=Field(...,pattern="^(low|medium|high)$")
class TaskUpdate(BaseModel):
    description:Optional[str]=Field(None,max_length=300)
    priority:Optional[str]=Field(None,pattern="^(low|medium|high)$")