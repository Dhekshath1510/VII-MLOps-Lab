from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI(title="Wine Quality Prediction API")


# Load trained model
with open("model/model.pkl", "rb") as file:
    model = pickle.load(file)


@app.get("/")
def home():
    return {
        "message": "Wine Quality Prediction API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/predict")
def predict(features: list):

    data = np.array(features).reshape(1, -1)

    prediction = model.predict(data)

    return {
        "prediction": int(prediction[0])
    }