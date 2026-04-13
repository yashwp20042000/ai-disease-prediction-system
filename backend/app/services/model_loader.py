import joblib
import os

# Define BASE_DIR correctly (points to project root)
BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../")
)

# Model paths
model_path = os.path.join(BASE_DIR, "models", "trained_model.pkl")
scaler_path = os.path.join(BASE_DIR, "models", "scaler.pkl")

# Safety check
if not os.path.exists(model_path) or not os.path.exists(scaler_path):
    raise Exception("Model or scaler not found. Please run training first.")

# Load model
model = joblib.load(model_path)
scaler = joblib.load(scaler_path)