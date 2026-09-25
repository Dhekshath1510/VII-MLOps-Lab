import os
import mlflow
import mlflow.sklearn
import mlflow.xgboost

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    ConfusionMatrixDisplay
)

from xgboost import XGBClassifier


# ---------------------------------------------------------
# 1. Create output directory
# ---------------------------------------------------------

OUTPUT_DIR = "../outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)


# ---------------------------------------------------------
# 2. Load Wine Quality Dataset
# ---------------------------------------------------------

url = (
    "https://archive.ics.uci.edu/ml/machine-learning-databases/"
    "wine-quality/winequality-red.csv"
)

df = pd.read_csv(url, sep=";")

print("Dataset loaded successfully.")
print("Dataset shape:", df.shape)


# ---------------------------------------------------------
# 3. Convert Wine Quality into Binary Classification
# ---------------------------------------------------------
# Quality >= 6 -> Good Wine (1)
# Quality < 6  -> Bad Wine (0)

df["quality_label"] = (df["quality"] >= 6).astype(int)

X = df.drop(columns=["quality", "quality_label"])
y = df["quality_label"]


# ---------------------------------------------------------
# 4. Train-Test Split
# ---------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# ---------------------------------------------------------
# 5. Feature Scaling
# ---------------------------------------------------------

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# ---------------------------------------------------------
# 6. MLflow Experiment
# ---------------------------------------------------------

mlflow.set_experiment("Wine_Quality_Multi_Model_Tracking")


# ---------------------------------------------------------
# 7. Define Models
# ---------------------------------------------------------

models = {
    "Logistic Regression": LogisticRegression(
        max_iter=1000,
        random_state=42
    ),

    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        random_state=42
    ),

    "XGBoost": XGBClassifier(
        n_estimators=100,
        max_depth=5,
        learning_rate=0.1,
        random_state=42,
        eval_metric="logloss"
    )
}


# ---------------------------------------------------------
# 8. Train and Track Models
# ---------------------------------------------------------

results = []


for model_name, model in models.items():

    print("\n" + "=" * 60)
    print("Training:", model_name)
    print("=" * 60)

    # Use scaled data for Logistic Regression
    if model_name == "Logistic Regression":
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_test_scaled)
        y_prob = model.predict_proba(X_test_scaled)[:, 1]

    else:
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        y_prob = model.predict_proba(X_test)[:, 1]

    # -----------------------------------------------------
    # Calculate Metrics
    # -----------------------------------------------------

    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_prob)

    print("Accuracy :", round(accuracy, 4))
    print("F1 Score :", round(f1, 4))
    print("ROC-AUC  :", round(roc_auc, 4))


    # -----------------------------------------------------
    # Start MLflow Run
    # -----------------------------------------------------

    with mlflow.start_run(run_name=model_name):

        # Log model name
        mlflow.log_param("model", model_name)

        # Log hyperparameters
        params = model.get_params()

        for param_name, param_value in params.items():
            try:
                mlflow.log_param(param_name, param_value)
            except Exception:
                pass

        # Log metrics
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("f1_score", f1)
        mlflow.log_metric("roc_auc", roc_auc)

        # -------------------------------------------------
        # Confusion Matrix
        # -------------------------------------------------

        cm = confusion_matrix(y_test, y_pred)

        display = ConfusionMatrixDisplay(
            confusion_matrix=cm,
            display_labels=["Bad Wine", "Good Wine"]
        )

        display.plot()

        plt.title(f"Confusion Matrix - {model_name}")
        plt.tight_layout()

        safe_name = model_name.lower().replace(" ", "_")

        cm_path = os.path.join(
            OUTPUT_DIR,
            f"confusion_matrix_{safe_name}.png"
        )

        plt.savefig(cm_path)
        plt.close()

        # Log confusion matrix as MLflow artifact
        mlflow.log_artifact(cm_path)

        # Log model
        if model_name == "XGBoost":
            mlflow.xgboost.log_model(
                model,
                "model"
            )
        else:
            mlflow.sklearn.log_model(
                model,
                "model"
            )

        # Store run information
        run_id = mlflow.active_run().info.run_id

        results.append({
            "model": model_name,
            "accuracy": accuracy,
            "f1_score": f1,
            "roc_auc": roc_auc,
            "run_id": run_id
        })


# ---------------------------------------------------------
# 9. Create Results DataFrame
# ---------------------------------------------------------

results_df = pd.DataFrame(results)

print("\n")
print("=" * 60)
print("MODEL COMPARISON")
print("=" * 60)

print(results_df)


# ---------------------------------------------------------
# 10. Select Best Model using MLflow Client API
# ---------------------------------------------------------

client = mlflow.MlflowClient()

experiment = client.get_experiment_by_name(
    "Wine_Quality_Multi_Model_Tracking"
)

runs = client.search_runs(
    experiment_ids=[experiment.experiment_id],
    order_by=["metrics.roc_auc DESC"]
)


# ---------------------------------------------------------
# 11. Get Best Run
# ---------------------------------------------------------

best_run = runs[0]

best_model_name = best_run.data.params.get("model")
best_accuracy = best_run.data.metrics.get("accuracy")
best_f1 = best_run.data.metrics.get("f1_score")
best_roc_auc = best_run.data.metrics.get("roc_auc")
best_run_id = best_run.info.run_id


# ---------------------------------------------------------
# 12. Display Best Model
# ---------------------------------------------------------

print("\n")
print("=" * 60)
print("BEST MODEL")
print("=" * 60)

print("Model     :", best_model_name)
print("Accuracy  :", round(best_accuracy, 4))
print("F1 Score  :", round(best_f1, 4))
print("ROC-AUC   :", round(best_roc_auc, 4))
print("Run ID    :", best_run_id)


# ---------------------------------------------------------
# 13. Save Best Model Information
# ---------------------------------------------------------

best_model_file = os.path.join(
    OUTPUT_DIR,
    "best_model.txt"
)

with open(best_model_file, "w") as file:

    file.write("Best Model Selected using MLflow Client API\n")
    file.write("=" * 50 + "\n")
    file.write(f"Model: {best_model_name}\n")
    file.write(f"Accuracy: {best_accuracy:.4f}\n")
    file.write(f"F1 Score: {best_f1:.4f}\n")
    file.write(f"ROC-AUC: {best_roc_auc:.4f}\n")
    file.write(f"Run ID: {best_run_id}\n")


print("\nBest model information saved to:")
print(best_model_file)

print("\nExperiment completed successfully!")