from fastapi import FastAPI
from pathlib import Path
from pydantic import BaseModel
import pickle
import numpy as np
import redis
import json
import os

app = FastAPI()


MODEL_PATH = Path(__file__).parent / "salary_model.pkl"

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)


class Data(BaseModel):
    age: int
    hours: int
    exp: int

def get_cache():
    return redis.Redis(
        host=os.getenv("REDIS_HOST", "localhost"), port=6379, decode_responses=True
    )

@app.get("/")
def home():
    return {"message": "ML API running with Redis + Docker Compose"}

@app.post("/predict")
def predict(data: Data):

    cache = get_cache()
    key = f"{data.age}:{data.hours}:{data.exp}"

    # Check cache
    cached_result = cache.get(key)
    if cached_result:
        return {"source": "cache", "prediction": json.loads(cached_result)}

    # ML prediction
    input_data = np.array([[data.age, data.hours, data.exp]])
    prediction = model.predict(input_data)[0]

    result = float(prediction)

    # Store in cache
    cache.set(key, json.dumps(result))

    return {"source": "model", "prediction": result}
