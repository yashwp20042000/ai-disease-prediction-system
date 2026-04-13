import requests
import os

API_URL = os.getenv("API_URL", "http://localhost:8000/predict")

def get_prediction(data):
    response = requests.post(API_URL, json=data)
    return response.json()