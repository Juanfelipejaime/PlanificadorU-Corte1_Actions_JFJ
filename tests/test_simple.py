import pytest
import sys
import os
sys.path.insert(0, os.path.abspath('.'))

from backend.app import create_app

def test_health():
    app = create_app()
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200
    assert b'healthy' in response.data

def test_api_info():
    app = create_app()
    client = app.test_client()
    response = client.get('/api/info')
    assert response.status_code == 200
    assert b'Planificador' in response.data
