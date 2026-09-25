import mlflow
from mlflow import MlflowClient
from sklearn.datasets import load_iris


# ---------------------------------------------------------
# 1. MLflow Client
# ---------------------------------------------------------

client = MlflowClient()

EXPERIMENT_NAME = "Wine_Quality_Multi_Model_Tracking"
MODEL_NAME = "WineQuality-BestModel"

ACCURACY_THRESHOLD = 0.70


# ---------------------------------------------------------
# 2. Find Experiment
# ---------------------------------------------------------

experiment = client.get_experiment_by_name(EXPERIMENT_NAME)

if experiment is None:
    raise Exception("MLflow experiment not found.")

print("Experiment found:", EXPERIMENT_NAME)


# ---------------------------------------------------------
# 3. Find Best Model
# ---------------------------------------------------------

runs = client.search_runs(
    experiment_ids=[experiment.experiment_id],
    order_by=["metrics.roc_auc DESC"]
)

if not runs:
    raise Exception("No MLflow runs found.")

best_run = runs[0]

run_id = best_run.info.run_id
accuracy = best_run.data.metrics.get("accuracy", 0)

print("Best Run ID:", run_id)
print("Accuracy:", accuracy)


# ---------------------------------------------------------
# 4. Validation Gate
# ---------------------------------------------------------

if accuracy <= ACCURACY_THRESHOLD:
    print("Validation failed.")
    print("Model was not registered because accuracy is below threshold.")
    exit()

print("Validation passed.")


# ---------------------------------------------------------
# 5. Register Model
# ---------------------------------------------------------

model_uri = f"runs:/{run_id}/model"

try:
    registered_model = client.create_registered_model(
        MODEL_NAME,
        description="Best Wine Quality classification model selected using MLflow."
    )

    print("Registered model created.")

except Exception:
    print("Registered model already exists.")


model_version = client.create_model_version(
    name=MODEL_NAME,
    source=model_uri,
    run_id=run_id
)

version = model_version.version

print("Model Version:", version)


# ---------------------------------------------------------
# 6. Add Description and Tags
# ---------------------------------------------------------

client.update_model_version(
    name=MODEL_NAME,
    version=version,
    description="Validated best model for Wine Quality classification."
)

client.set_model_version_tag(
    name=MODEL_NAME,
    version=version,
    key="validation",
    value="passed"
)

client.set_model_version_tag(
    name=MODEL_NAME,
    version=version,
    key="model_type",
    value=best_run.data.params.get("model", "Unknown")
)


# ---------------------------------------------------------
# 7. Transition Model Lifecycle
# ---------------------------------------------------------

# None → Staging
client.transition_model_version_stage(
    name=MODEL_NAME,
    version=version,
    stage="Staging"
)

print("Model transitioned to: Staging")


# Staging → Production
client.transition_model_version_stage(
    name=MODEL_NAME,
    version=version,
    stage="Production"
)

print("Model transitioned to: Production")


# ---------------------------------------------------------
# 8. Load Production Model
# ---------------------------------------------------------

production_model_uri = f"models:/{MODEL_NAME}/Production"

production_model = mlflow.sklearn.load_model(
    production_model_uri
)

print("Production model loaded successfully.")


# ---------------------------------------------------------
# 9. Batch Inference
# ---------------------------------------------------------

iris = load_iris()

sample_data = iris.data[:10]

predictions = production_model.predict(sample_data)

print("\nBatch Inference Results:")
print(predictions)


# ---------------------------------------------------------
# 10. Save Output
# ---------------------------------------------------------

with open("../output/result.txt", "w") as file:

    file.write("MLflow Model Registry Lifecycle\n")
    file.write("================================\n\n")

    file.write(f"Experiment: {EXPERIMENT_NAME}\n")
    file.write(f"Best Run ID: {run_id}\n")
    file.write(f"Accuracy: {accuracy:.4f}\n")
    file.write(f"Validation Threshold: {ACCURACY_THRESHOLD}\n")
    file.write("Validation: PASSED\n\n")

    file.write(f"Registered Model: {MODEL_NAME}\n")
    file.write(f"Model Version: {version}\n")
    file.write("Lifecycle: None -> Staging -> Production\n")
    file.write("Production model loaded successfully.\n\n")

    file.write("Batch Inference Predictions:\n")
    file.write(str(predictions.tolist()))

print("\nExperiment completed successfully.")