from fastapi import APIRouter
from pydantic import BaseModel
from services.ml_service import predict_priority
router = APIRouter()

class PredictionRequest(BaseModel):
    title:str

@router.post("/predict-priority")
def predict(data:PredictionRequest):
    result=predict_priority(data.title)
    return{
        "Predicted-priority":result
    }
