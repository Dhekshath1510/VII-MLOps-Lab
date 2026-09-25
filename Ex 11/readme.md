# Ex 6 – FastAPI Serving App with Integration Tests

## Aim

To develop a FastAPI machine learning serving application with Pydantic input validation and perform integration testing using pytest and httpx.

## Objective

* Create a FastAPI ML prediction application.
* Define a Pydantic input schema.
* Implement `/predict`, `/health`, and `/model-info` endpoints.
* Return prediction and confidence from the prediction endpoint.
* Display model version and status through the health endpoint.
* Write asynchronous integration tests using pytest and httpx.
* Run the integration tests inside Docker.

## Software Requirements

* Python
* FastAPI
* Pydantic
* Pytest
* HTTPX
* Docker
* Scikit-learn

## API Endpoints

### `/predict`

Accepts model input features and returns:

* Prediction
* Confidence

### `/health`

Returns:

* Application status
* Model version

### `/model-info`

Returns:

* Model name
* Model version
* Model description

## Testing

Integration tests were written using `pytest` and `httpx.AsyncClient`.

The following endpoints were tested:

1. Health endpoint
2. Model information endpoint
3. Prediction endpoint

Tests can be executed using:

```bash
pytest -v
```

The tests can also be executed inside Docker:

```bash
docker build -t fastapi-ml-test .
docker run --rm fastapi-ml-test pytest -v
```

## Result

The FastAPI machine learning serving application was successfully created with Pydantic validation and the required API endpoints. Integration tests were successfully written using pytest and HTTPX and executed inside a Docker container.

## Conclusion

A FastAPI-based ML serving application with health monitoring, model information, prediction confidence, input validation, and automated integration testing was successfully implemented.
