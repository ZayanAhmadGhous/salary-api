# Salary Prediction API with FastAPI, Redis & Docker Compose

## Overview

This project demonstrates a complete Machine Learning API deployment workflow using FastAPI, Redis, Docker, and Docker Compose.

A machine learning model is trained to predict salary based on:

* Age
* Working Hours
* Experience

The model is exposed through a REST API built with FastAPI. Redis is used as a caching layer to store previous predictions and improve response time. Docker and Docker Compose are used to containerize and orchestrate the application.

---

## Tech Stack

* Python
* FastAPI
* Scikit-Learn
* NumPy
* Redis
* Docker
* Docker Compose

---

## Project Architecture

```text
                ┌──────────────┐
                │    Client    │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │   FastAPI    │
                └──────┬───────┘
                       │
          ┌────────────┴────────────┐
          │                         │
          ▼                         ▼
   Redis Cache              ML Prediction Model
          │                         │
          └────────────┬────────────┘
                       ▼
                  API Response
```

---

## Features

* REST API using FastAPI
* Machine Learning salary prediction
* Redis caching for faster repeated requests
* Dockerized application
* Multi-container setup using Docker Compose
* Production-style project structure

---

## Project Structure

```text
salary_api/
│
├── app/
│   ├── main.py
│   └── salary_model.pkl
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## API Endpoint

### Home Endpoint

```http
GET /
```

Response:

```json
{
  "message": "ML API running with Redis + Docker Compose"
}
```

---

### Salary Prediction Endpoint

```http
POST /predict
```

Parameters:

| Parameter | Type |
| --------- | ---- |
| age       | int  |
| hours     | int  |
| exp       | int  |

Example:

```http
POST /predict?age=25&hours=8&exp=3
```

Response:

```json
{
  "source": "model",
  "prediction": 45000.25
}
```

Cached Response:

```json
{
  "source": "cache",
  "prediction": 45000.25
}
```

---

## Redis Caching Workflow

1. User sends prediction request.
2. API creates a unique cache key.
3. Redis is checked for existing prediction.
4. If found:

   * Return cached result.
5. If not found:

   * Run ML model.
   * Store result in Redis.
   * Return prediction.

---

## Running Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run FastAPI:

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://localhost:8000/docs
```

---

## Running with Docker

Build image:

```bash
docker build -t salary-api .
```

Run container:

```bash
docker run -p 8000:8000 salary-api
```

---

## Running with Docker Compose

Start all services:

```bash
docker compose up --build
```

Stop services:

```bash
docker compose down
```

Open Swagger UI:

```text
http://localhost:8000/docs
```

---

## Environment Variables

| Variable   | Description    |
| ---------- | -------------- |
| REDIS_HOST | Redis hostname |

Example:

```python
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
```

Docker Compose automatically sets:

```yaml
environment:
  - REDIS_HOST=redis
```

---

## Learning Outcomes

This project helped me understand:

* Model deployment with FastAPI
* Building REST APIs for ML models
* Redis caching fundamentals
* Docker containerization
* Docker Compose orchestration
* Service-to-service communication
* Production-style MLOps workflows

---

## Future Improvements

* Kubernetes Deployment
* CI/CD Pipeline
* Model Versioning
* Monitoring & Logging
* Cloud Deployment (AWS/GCP/Azure)
* Automated Retraining Pipeline

---

## Author

**Zayan Ahmad**

Aspiring AI Engineer | MLOps Learner | Machine Learning Enthusiast

GitHub: https://github.com/ZayanAhmadGhous
