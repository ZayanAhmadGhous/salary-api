from fastapi.testclient import TestClient
from unittest.mock import MagicMock
import app.main as main
from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"]


def test_predict(monkeypatch):

    # Fake Redis
    mock_cache = MagicMock()
    mock_cache.get.return_value = None
    mock_cache.set.return_value = True

    # Replace real Redis with fake one
    monkeypatch.setattr(main, "get_cache", lambda: mock_cache)

    response = client.post("/predict", json={"age": 20, "hours": 8, "exp": 2})

    assert response.status_code == 200

    data = response.json()
    assert "prediction" in data
    assert "source" in data
