from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_model1_endpoint():
    response = client.post(
        "/model1",
        json={"input": "test"},
        headers={"X-API-Key": "test_api_key"}
    )
    assert response.status_code == 200
    assert "result" in response.json()