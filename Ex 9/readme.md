# Ex 4 – MLflow Model Registry Lifecycle

## Aim

To register the best machine learning model using the MLflow Model Registry and demonstrate its lifecycle from None to Staging and Production with a validation gate.

## Objective

* Identify the best model from the previous MLflow experiment.
* Register the model using the MLflow Python API.
* Add model description and tags.
* Validate the model using an accuracy threshold.
* Transition the model from None to Staging and Production.
* Load the Production model.
* Perform batch inference.

## Software Requirements

* Python
* MLflow
* Scikit-learn
* Pandas

## Procedure

1. Connect to the MLflow tracking server using the MLflow Client API.
2. Retrieve the best model run from the previous experiment.
3. Check whether the model accuracy satisfies the validation threshold.
4. Register the validated model in the MLflow Model Registry.
5. Add a description and tags to the model version.
6. Transition the model through Staging to Production.
7. Load the Production model using its registered model URI.
8. Perform batch inference using sample Wine Quality data.

## Validation Gate

The model is promoted only when its accuracy is greater than the defined threshold.

```text
Accuracy > Threshold
       |
       v
   Validation
       |
       v
     Staging
       |
       v
   Production
```

## Result

The best model from the previous experiment was successfully registered in the MLflow Model Registry. The model passed the validation gate and was transitioned through Staging to Production. The Production model was successfully loaded and used for batch inference.

## Conclusion

The MLflow Model Registry lifecycle was successfully demonstrated using the MLflow Client API. Model metadata, validation, lifecycle stages, and Production inference were successfully managed.
