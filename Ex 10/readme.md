# Ex 5 – Production-Ready ML Docker Image

## Aim

To containerize a machine learning prediction API using Docker and FastAPI with a production-ready multi-stage Dockerfile.

## Objective

* Create a FastAPI-based ML prediction service.
* Build a multi-stage Docker image using Python 3.11 Slim.
* Install only the required production dependencies.
* Copy the trained model artifact into the image.
* Configure a Docker health check.
* Expose port 8000.
* Build and run the Docker container.
* Test the prediction API using curl.
* Push the Docker image to Docker Hub.

## Software Requirements

* Docker
* Python
* FastAPI
* Scikit-learn
* curl
* Docker Hub

## Procedure

### 1. Build Docker Image

```bash
docker build -t wine-quality-api .
```

### 2. Run Container

```bash
docker run -d -p 8000:8000 --name wine-api wine-quality-api
```

### 3. Verify Health

```bash
curl http://localhost:8000/health
```

Expected response:

```text
{"status":"healthy"}
```

### 4. Test Prediction

```bash
curl -X POST http://localhost:8000/predict \
-H "Content-Type: application/json" \
-d "[7.4,0.7,0,1.9,0.076,11,34,0.9978,3.51,0.56,9.4]"
```

### 5. Check Container Health

```bash
docker ps
```

The container should show a healthy status after the health check succeeds.

### 6. Tag Docker Image

```bash
docker tag wine-quality-api <dockerhub-username>/wine-quality-api:latest
```

### 7. Login to Docker Hub

```bash
docker login
```

### 8. Push Image

```bash
docker push <dockerhub-username>/wine-quality-api:latest
```

## Result

The machine learning model was successfully packaged into a production-ready Docker image. The FastAPI service was started inside the container, the health check was verified, and predictions were successfully tested using curl. The Docker image was also prepared for deployment through Docker Hub.

## Conclusion

A production-ready ML API was successfully containerized using a multi-stage Docker build. The application includes production dependencies, model artifacts, health monitoring, API access through port 8000, and Docker Hub deployment support.
