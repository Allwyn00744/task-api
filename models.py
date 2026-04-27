from sqlalchemy import Column,String,Integer,Boolean,ForeignKey
from database import Base

class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)

class TaskModel(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    user_priority = Column(String, nullable=True)
    predicted_priority = Column(String, nullable=True)
    final_priority = Column(String, nullable=False)
    is_deleted = Column(Boolean, default=False)

    user_id = Column(Integer, ForeignKey("users.id"), index=True)