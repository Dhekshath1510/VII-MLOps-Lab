from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np


app = FastAPI(title="Wine Quality Prediction API")

MODEL_VERSION = "1.0.0"


# Load trained model
with open("model/model.pkl", "rb") as file:
    model = pickle.load(file)


# ---------------------------------------------------------
# Pydantic Input Schema
# ---------------------------------------------------------

class PredictionInput(BaseModel):
    features: list[float]


# ---------------------------------------------------------
# Health Endpoint
# ---------------------------------------------------------

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model_version": MODEL_VERSION
    }


# ---------------------------------------------------------
# Model Information
# ---------------------------------------------------------

@app.get("/model-info")
def model_info():
    return {
        "model": type(model).__name__,
        "version": MODEL_VERSION,
        "description": "Wine Quality Classification Model"
    }


# ---------------------------------------------------------
# Prediction Endpoint
# ---------------------------------------------------------

@app.post("/predict")
def predict(input_data: PredictionInput):

    features = np.array(input_data.features).reshape(1, -1)

    prediction = model.predict(features)[0]

    # Prediction confidence
    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(features)[0]
        confidence = float(max(probabilities))
    else:
        confidence = 1.0

    return {
        "prediction": int(prediction),
        "confidence": round(confidence, 4)
    }


# ---------------------------------------------------------
# Root Endpoint
# ---------------------------------------------------------

@app.get("/")
def root():
    return {
        "message": "FastAPI ML Serving App is running"
    }