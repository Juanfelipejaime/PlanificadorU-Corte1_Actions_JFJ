import asyncio
from backend.app import create_app

def test_saludo():
    # Crear un event loop manual para evitar el error
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    app = create_app()
    client = app.test_client()

    response = client.get('/health')
    assert response.status_code == 200
    assert b'healthy' in response.data

def test_api_info():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    app = create_app()
    client = app.test_client()

    response = client.get('/api/info')
    assert response.status_code == 200
