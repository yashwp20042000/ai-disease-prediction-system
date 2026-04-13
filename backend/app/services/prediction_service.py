import numpy as np
from app.services.model_loader import model, scaler

def make_prediction(data):
    try:
        input_data = [
            data.pregnancies,
            data.glucose,
            data.blood_pressure,
            data.skin_thickness,
            data.insulin,
            data.bmi,
            data.diabetes_pedigree,
            data.age
        ]

        arr = np.array(input_data).reshape(1, -1)
        arr_scaled = scaler.transform(arr)

        prediction = model.predict(arr_scaled)[0]
        return int(prediction)

    except Exception as e:
        return {"error": str(e)}