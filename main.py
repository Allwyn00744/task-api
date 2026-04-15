from fastapi import FastAPI
from database import engine,Base
from routes.task_routes import router 
import models


app=FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)