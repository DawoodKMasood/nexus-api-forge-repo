from fastapi.testclient import TestClient
from app.main import app
from app.config import settings
import time

client = TestClient(app)

def test_rate_limiting():
    for _ in range(settings.RATE_LIMIT):
        response = client.post(
            "/model1",
            json={"input": "test"},
            headers={"X-API-Key": "test_api_key"}
        )
        assert response.status_code == 200
    
    response = client.post(
        "/model1",
        json={"input": "test"},
        headers={"X-API-Key": "test_api_key"}
    )
    assert response.status_code == 429
    assert response.json() == {"detail": "Rate limit exceeded"}