import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib
from preprocessing import preprocess_data
import os

if not os.path.exists("data/raw/diabetes.csv"):
    raise FileNotFoundError("Dataset not found. Please add diabetes.csv in data/raw/")

# Load dataset
df = pd.read_csv("data/raw/diabetes.csv")

X, y, scaler = preprocess_data(df)

model = LogisticRegression()
model.fit(X, y)

# Save model
joblib.dump(model, "models/trained_model.pkl")
joblib.dump(scaler, "models/scaler.pkl")

print("Model trained and saved.")