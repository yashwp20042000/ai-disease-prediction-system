from fastapi import FastAPI
from app.routes import predict, health

app = FastAPI()

app.include_router(predict.router)
app.include_router(health.router)