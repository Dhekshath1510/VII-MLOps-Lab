# Ex 7 – End-to-End ML CI/CD with GitHub Actions

## Aim

To implement an end-to-end machine learning CI/CD pipeline using GitHub Actions with data validation, model evaluation, Docker image creation, and Kubernetes staging deployment.

## Objective

* Validate the dataset before model training.
* Train and evaluate the machine learning model.
* Apply an F1-score quality gate of 0.85.
* Build a Docker image using the Git commit SHA.
* Deploy the application to a Kubernetes staging environment.
* Execute jobs sequentially using GitHub Actions dependency gates.

## Software Requirements

* Python
* GitHub Actions
* Great Expectations
* Docker
* kubectl
* Scikit-learn
* Pandas
* Kubernetes

## Pipeline Jobs

The workflow contains four sequential jobs:

```text
Data Validation
       |
       v
Train and Evaluate
       |
       v
Build Docker
       |
       v
Deploy Staging
```

### Job 1 – Data Validation

The dataset is checked before model training. The workflow verifies that the dataset is available and contains the required columns.

### Job 2 – Train and Evaluate

A Random Forest classifier is trained and evaluated using the F1 score.

The pipeline continues only when:

```text
F1 Score >= 0.85
```

### Job 3 – Build Docker

A Docker image is created after successful model evaluation. The image is tagged using the Git commit SHA.

Example:

```bash
docker build -t ml-model:${GITHUB_SHA} .
```

### Job 4 – Deploy Staging

The Kubernetes deployment configuration is applied using:

```bash
kubectl apply -f k8s/deployment.yaml
```

## Dependency Gates

GitHub Actions `needs` is used to ensure that every stage executes only after the previous stage succeeds.

```yaml
train-and-evaluate:
  needs: data-validation

build-docker:
  needs: train-and-evaluate

deploy-staging:
  needs: build-docker
```

## Result

An end-to-end four-job machine learning CI/CD pipeline was successfully created using GitHub Actions. Dataset validation, model evaluation with an F1 quality gate, Docker image building, and Kubernetes staging deployment were integrated into a sequential workflow.

## Conclusion

The experiment demonstrated how machine learning workflows can be automated using CI/CD practices. Dependency gates ensure that only validated data and models proceed to Docker image creation and staging deployment.
