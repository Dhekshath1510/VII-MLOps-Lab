import json

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score


# Load dataset
df = pd.read_csv("data/wine.csv")

# Convert quality into binary classification
df["quality_label"] = (df["quality"] >= 6).astype(int)

X = df.drop(columns=["quality", "quality_label"])
y = df["quality_label"]


# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)


# Prediction
predictions = model.predict(X_test)


# F1 Score
f1 = f1_score(y_test, predictions)

print("F1 Score:", round(f1, 4))


# Save metrics
metrics = {
    "f1_score": round(f1, 4)
}

with open("metrics.json", "w") as file:
    json.dump(metrics, file, indent=4)

print("Metrics saved successfully.")