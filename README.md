# FastAPI MLOps Microservice

A containerized Machine Learning API built with **FastAPI, scikit-learn, Poetry, Docker, and pytest**.

This project demonstrates how a trained machine learning model can be exposed through a REST API, tested with automated tests, and packaged into a Docker container for reproducible execution.

## Features

- FastAPI REST API for machine learning predictions
- scikit-learn Random Forest model
- Automatic feature ordering based on the trained model schema
- Health-check endpoint
- Poetry dependency management
- Docker containerization
- Automated API and service tests with pytest
- Swagger/OpenAPI documentation
- MIT licensed and based on an existing MLOps tutorial/project

## Architecture

```text
Client
  |
  v
FastAPI
  |
  +---- GET /api/v1/health
  |
  +---- POST /api/v1/predict
              |
              v
       PredictionService
              |
              v
       Trained ML Model
              |
              v
          Prediction

Project Structure:

mlops-fastapi-microservice/
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── models/
│   └── model.pkl
│
├── src/
│   ├── api/
│   │   └── v1/
│   │       └── routes.py
│   │
│   ├── app/
│   │   └── services/
│   │       └── model_service.py
│   │
│   └── core/
│       ├── config.py
│       └── server.py
│
├── tests/
│   ├── test_api.py
│   └── test_services.py
│
├── Dockerfile
├── docker-compose.yaml
├── poetry.lock
├── pyproject.toml
├── train_model.py
├── LICENSE
└── README.md


API Endpoints
Health Check:

GET /api/v1/health

{
  "status": "healthy"
}

Prediction:

POST /api/v1/predict

{
  "features": {
    "sepal length (cm)": 5.1,
    "sepal width (cm)": 3.5,
    "petal length (cm)": 1.4,
    "petal width (cm)": 0.2
  }
}

{
  "prediction": [0]
}


Swagger API Documentation

After starting the application, open:

http://127.0.0.1:8000/docs

1. Install Dependencies

Install Poetry:
pip install poetry
poetry install --no-root

2. Start the Application:
poetry run uvicorn src.core.server:app --reload
http://127.0.0.1:8000
http://127.0.0.1:8000/docs

Running Tests
Windows PowerShell:

$env:PYTHONPATH="."
poetry run pytest

Linux/macOS
PYTHONPATH=. poetry run pytest

Docker
Build the Docker Image
docker build -t mlops-fastapi .
Run the Container
docker run -d --name mlops-api -p 8000:8000 mlops-fastapi

Check the running container:

docker ps
Test the Health Endpoint
http://localhost:8000/api/v1/health

Expected response:

{
  "status": "healthy"
}
Test the Prediction Endpoint

Send a POST request to:

http://localhost:8000/api/v1/predict

Example input:

{
  "features": {
    "sepal length (cm)": 5.1,
    "sepal width (cm)": 3.5,
    "petal length (cm)": 1.4,
    "petal width (cm)": 0.2
  }
}

Example response:

{
  "prediction": [0]
}
Implementation Improvements

The original project was modified and tested locally as part of this implementation.

Feature Schema Handling

The prediction service retrieves the feature names stored by the trained scikit-learn model and reorders incoming API features accordingly.

This prevents prediction failures when incoming features are supplied in a different order from the order used during model training.

Health Monitoring Endpoint

Added:

GET /api/v1/health

This provides a lightweight endpoint for checking whether the API service is responding.

Automated Testing

The API test suite was extended to verify the health endpoint while retaining the existing prediction and root endpoint tests.

Verification

The modified application was verified through:

Local pytest        → 4 passed
Docker image build  → Successful
Docker container    → Running
Health API          → 200 OK
Prediction API      → 200 OK
Original Project and Attribution

This implementation is based on the existing open-source project/tutorial structure and has been modified for learning and development purposes.

Original tutorial:

The Halftime Code — FastAPI for MLOps: Integrate Docker, Poetry, and Deploy to AWS EC2

https://www.thehalftimecode.com/fastapi-for-mlops-integrate-docker-poetry-and-deploy-to-aws-ec2/

The original repository's MIT License is retained in this project.

License

This project is licensed under the MIT License. See the LICENSE file for details.


