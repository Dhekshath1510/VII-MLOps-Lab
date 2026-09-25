# Ex 2 – MLflow Multi-Model Experiment Tracking

## Aim

To train and compare Logistic Regression, Random Forest, and XGBoost models on the Wine Quality dataset using MLflow for experiment tracking.

## Objective

* Train three machine learning classification models.
* Track model hyperparameters using MLflow.
* Log Accuracy, F1 Score, and ROC-AUC metrics.
* Generate and track confusion matrix plots.
* Select the best-performing model programmatically using the MLflow Client API.

## Software Requirements

* Python
* Pandas
* Scikit-learn
* XGBoost
* MLflow
* Matplotlib

## Models Used

1. Logistic Regression
2. Random Forest
3. XGBoost

## Procedure

1. Load the Wine Quality dataset.
2. Convert the wine quality values into binary classes.
3. Split the dataset into training and testing sets.
4. Train Logistic Regression, Random Forest, and XGBoost model# Ex 2 – MLflow Multi-Model Experiment Tracking

## Aim

To train and compare Logistic Regression, Random Forest, and XGBoost models on the Wine Quality dataset using MLflow for experiment tracking.

## Objective

* Train three machine learning classification models.
* Track model hyperparameters using MLflow.
* Log Accuracy, F1 Score, and ROC-AUC metrics.
* Generate and track confusion matrix plots.
* Select the best-performing model programmatically using the MLflow Client API.

## Software Requirements

* Python
* Pandas
* Scikit-learn
* XGBoost
* MLflow
* Matplotlib

## Models Used

1. Logistic Regression
2. Random Forest
3. XGBoost

## Procedure

1. Load the Wine Quality dataset.
2. Convert the wine quality values into binary classes.
3. Split the dataset into training and testing sets.
4. Train Logistic Regression, Random Forest, and XGBoost models.
5. Start an MLflow run for each model.
6. Log model hyperparameters.
7. Calculate Accuracy, F1 Score, and ROC-AUC.
8. Generate confusion matrix plots and log them as MLflow artifacts.
9. Compare the recorded model metrics using the MLflow Client API.
10. Select the model with the highest ROC-AUC score.

## Result

The three classification models were successfully trained and tracked using MLflow. Their hyperparameters, evaluation metrics, and confusion matrix plots were logged successfully. The best-performing model was selected programmatically using the MLflow Client API.

## Conclusion

MLflow was successfully used to track and compare multiple machine learning experiments. The experiment demonstrated how model parameters, performance metrics, and artifacts can be managed centrally and how the best model can be selected programmatically.
s.
5. Start an MLflow run for each model.
6. Log model hyperparameters.
7. Calculate Accuracy, F1 Score, and ROC-AUC.
8. Generate confusion matrix plots and log them as MLflow artifacts.
9. Compare the recorded model metrics using the MLflow Client API.
10. Select the model with the highest ROC-AUC score.

## Result

The three classification models were successfully trained and tracked using MLflow. Their hyperparameters, evaluation metrics, and confusion matrix plots were logged successfully. The best-performing model was selected programmatically using the MLflow Client API.

## Conclusion

MLflow was successfully used to track and compare multiple machine learning experiments. The experiment demonstrated how model parameters, performance metrics, and artifacts can be managed centrally and how the best model can be selected programmatically.
