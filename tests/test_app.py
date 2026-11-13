from app import app


def test_health_endpoint_returns_ok():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_home_page_returns_welcome():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to homelab-app" in response.data


def test_unknown_route_returns_404():
    client = app.test_client()
    response = client.get("/does-not-exist")
    assert response.status_code == 404
