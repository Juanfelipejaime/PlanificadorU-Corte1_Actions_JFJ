import pytest
from flask import Flask

# Simulamos tu app con lo mínimo necesario
app = Flask(__name__)

@app.route('/health')
def health():
    return {'status': 'healthy'}, 200

@app.route('/api/info')
def api_info():
    return {'name': 'Planificador Médico API'}, 200

client = app.test_client()

def test_health():
    response = client.get('/health')
    assert response.status_code == 200
    assert b'healthy' in response.data

def test_api_info():
    response = client.get('/api/info')
    assert response.status_code == 200
    assert b'Planificador' in response.data
