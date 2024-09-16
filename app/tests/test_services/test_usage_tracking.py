from fastapi.testclient import TestClient
from app.main import app
from app.database import get_db
from unittest.mock import patch

client = TestClient(app)

def test_usage_tracking():
    with patch('app.services.usage_tracking.track_usage') as mock_track_usage:
        response = client.post(
            "/model1",
            json={"input": "test"},
            headers={"X-API-Key": "test_api_key"}
        )
        assert response.status_code == 200
        mock_track_usage.assert_called_once()