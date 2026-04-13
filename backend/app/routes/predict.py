from fastapi import APIRouter
from app.schemas.request_schema import PredictionRequest
from app.services.prediction_service import make_prediction

router = APIRouter()

@router.post("/predict")
def predict(data: PredictionRequest):
    result = make_prediction(data)
    return {"prediction": result}