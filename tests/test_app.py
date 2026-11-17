from app import app


def test_health_endpoint_returns_ok():
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'ok'
    assert 'version' in data


def test_home_page_returns_welcome():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to homelab-app' in response.data


def test_unknown_route_returns_404():
    client = app.test_client()
    response = client.get('/does-not-exist')
    assert response.status_code == 404


def test_metrics_endpoint_exposes_prometheus_format():
    client = app.test_client()
    client.get('/health')
    response = client.get('/metrics')
    assert response.status_code == 200
    assert b'flask_http_request_total' in response.data
