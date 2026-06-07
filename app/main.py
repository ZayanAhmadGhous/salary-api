from fastapi import FastAPI
import pickle
import numpy as np
import redis
import json
import os



app = FastAPI()

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")

cache = redis.Redis(
    host=REDIS_HOST,
    port=6379,
    decode_responses=True
)


# Load ML model
with open("app/salary_model.pkl", "rb") as f:
    model = pickle.load(f)


@app.get("/")
def home():
    return {"message": "ML API running with Redis + Docker Compose"}


@app.post("/predict")
def predict(age: int, hours: int, exp: int):

    key = f"{age}:{hours}:{exp}"


    cached_result = cache.get(key)
    if cached_result:
        return {
            "source": "cache",
            "prediction": json.loads(cached_result)
        }


    input_data = np.array([[age, hours, exp]])
    prediction = model.predict(input_data)[0]


    cache.set(key, json.dumps(float(prediction)))

    return {
        "source": "model",
        "prediction": float(prediction)
    }