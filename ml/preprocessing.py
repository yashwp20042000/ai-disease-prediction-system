import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(df):
    df = df.dropna()
    X = df.drop("Outcome", axis=1)
    y = df["Outcome"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y, scaler