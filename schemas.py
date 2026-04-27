from pydantic import BaseModel,Field,EmailStr
from typing import Optional
class TaskCreate(BaseModel):
    title:str=Field(...,min_length=3,max_length=100)
    description:Optional[str]=Field(None,max_length=300)
    priority: Optional[str] = None
class TaskUpdate(BaseModel):
    description:Optional[str]=Field(None,max_length=300)
    priority:Optional[str]=Field(None,pattern="^(low|medium|high)$")
class UserRegister(BaseModel):
    name:str=Field(...,min_length=3,max_length=100)
    email:EmailStr
    password:str=Field(...,min_length=6)
class UserLogin(BaseModel):
    email:EmailStr
    password:str=Field(...,min_length=6)
class UserResponse(BaseModel):
    id:int
    name:str
    email:EmailStr
    class Config:
        from_attributes=True