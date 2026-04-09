import pytest
from app.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy", "message": "Service is operational"}

def test_get_data(client):
    response = client.get('/api/data')
    assert response.status_code == 200
    assert response.get_json() == {"data": "Secure information retrieved successfully."}

def test_security_headers(client):
    response = client.get('/health')
    assert response.headers.get('X-Content-Type-Options') == 'nosniff'
    assert response.headers.get('X-Frame-Options') == 'DENY'