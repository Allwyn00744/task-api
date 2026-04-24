from fastapi import FastAPI
from database import engine,Base
from routes.task_routes import router 
from routes.auth_routes import router as auth_router
import models


app=FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)
app.include_router(auth_router)