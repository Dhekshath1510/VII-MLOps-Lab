# Ex 3 – DVC Pipeline with Metric Versioning

## Aim

To create a three-stage DVC pipeline for data preparation, model training, and evaluation, and demonstrate dataset and metric versioning using Git and DVC.

## Objective

* Create a DVC pipeline with three stages.
* Version dataset iterations using Git and DVC.
* Train a machine learning model.
* Store evaluation metrics in JSON format.
* Use `dvc repro` to reproduce the pipeline.
* Compare metric changes between dataset versions using `dvc metrics diff`.

## Software Requirements

* Python
* DVC
* Git
* Pandas
* Scikit-learn
* JSON

## Pipeline Stages

```text
prepare
   ↓
train
   ↓
evaluate
```

### 1. Prepare

The dataset is loaded and preprocessed. The processed dataset is stored for the next stage.

### 2. Train

A Random Forest classification model is trained using the processed dataset.

### 3. Evaluate

The trained model is evaluated using Accuracy, and the result is stored in `metrics.json`.

## DVC Commands Used

Initialize DVC:

```bash
dvc init
```

Track the dataset:

```bash
dvc add data/wine.csv
```

Run the complete pipeline:

```bash
dvc repro
```

Check metrics:

```bash
dvc metrics show
```

Compare metrics between versions:

```bash
dvc metrics diff
```

## Dataset Versioning

The first dataset version was committed using Git and tracked using DVC. After modifying the dataset, a second version was created and committed separately.

Git and DVC were used together to maintain different dataset versions and reproduce the corresponding machine learning pipeline.

## Result

A three-stage DVC pipeline was successfully created using `prepare`, `train`, and `evaluate` stages. The model evaluation metric was stored in JSON format and metric changes between dataset versions could be compared using `dvc metrics diff`.

## Conclusion

DVC was successfully used for pipeline management, dataset versioning, reproducibility, and metric comparison. Git was used to maintain different versions of the experiment while DVC managed the machine learning data and pipeline dependencies.
