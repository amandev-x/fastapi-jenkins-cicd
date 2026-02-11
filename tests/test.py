from fastapi.testclient import TestClient 
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200 
    assert response.json()["status"] == "ok"

def test_create_item():
    response = client.post("/items", json={"name": "Test item", "price": 10.4})
    assert response.status_code == 201
    assert response.json()["message"] == "Item created successfully"