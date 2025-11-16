from fastapi.testclient import TestClient
from app.main import app
import pytest


client = TestClient(app)


def test_add_endpoint():
    resp = client.post("/add", json={"a": 5, "b": 3})
    assert resp.status_code == 200
    assert resp.json() == {"result": 8}


def test_divide_by_zero_returns_500():
    # operations.divide raises ZeroDivisionError -> caught as 500 by route
    resp = client.post("/divide", json={"a": 10, "b": 0})
    assert resp.status_code == 500
    assert "error" in resp.json()
