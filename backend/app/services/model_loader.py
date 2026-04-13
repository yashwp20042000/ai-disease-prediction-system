import joblib
import os

if not os.path.exists(os.path.join(BASE_DIR, "models/trained_model.pkl")):
    raise Exception("Model not found. Please run training first.")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

model = joblib.load(os.path.join(BASE_DIR, "models/trained_model.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "models/scaler.pkl"))