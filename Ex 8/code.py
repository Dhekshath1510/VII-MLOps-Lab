import sys
import os
import json
import pickle

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


DATA_FILE = "data/wine.csv"
PROCESSED_FILE = "data/processed.csv"
MODEL_FILE = "model/model.pkl"
METRICS_FILE = "metrics.json"


def prepare_data():

    os.makedirs("data", exist_ok=True)

    df = pd.read_csv(DATA_FILE)

    # Convert quality into binary classification
    df["quality_label"] = (df["quality"] >= 6).astype(int)

    df.to_csv(PROCESSED_FILE, index=False)

    print("Data preparation completed.")
    print("Processed data saved to:", PROCESSED_FILE)


def train_model():

    df = pd.read_csv(PROCESSED_FILE)

    X = df.drop(columns=["quality", "quality_label"])
    y = df["quality_label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    os.makedirs("model", exist_ok=True)

    with open(MODEL_FILE, "wb") as file:
        pickle.dump(model, file)

    # Save test data for evaluation
    test_data = X_test.copy()
    test_data["target"] = y_test.values
    test_data.to_csv("data/test.csv", index=False)

    print("Model training completed.")
    print("Model saved to:", MODEL_FILE)


def evaluate_model():

    df = pd.read_csv(PROCESSED_FILE)

    X = df.drop(columns=["quality", "quality_label"])
    y = df["quality_label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    with open(MODEL_FILE, "rb") as file:
        model = pickle.load(file)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    metrics = {
        "accuracy": round(accuracy, 4)
    }

    with open(METRICS_FILE, "w") as file:
        json.dump(metrics, file, indent=4)

    print("Evaluation completed.")
    print("Accuracy:", round(accuracy, 4))
    print("Metrics saved to:", METRICS_FILE)


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage:")
        print("python code/pipeline.py prepare")
        print("python code/pipeline.py train")
        print("python code/pipeline.py evaluate")
        sys.exit(1)

    stage = sys.argv[1]

    if stage == "prepare":
        prepare_data()

    elif stage == "train":
        train_model()

    elif stage == "evaluate":
        evaluate_model()

    else:
        print("Invalid stage.")