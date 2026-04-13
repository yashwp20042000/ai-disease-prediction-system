import joblib
import numpy as np

model = joblib.load("models/trained_model.pkl")
scaler = joblib.load("models/scaler.pkl")

def predict(data):
    data = np.array(data).reshape(1, -1)
    data_scaled = scaler.transform(data)
    prediction = model.predict(data_scaled)[0]
    return int(prediction)