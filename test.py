from fastapi.testclient import TestClient

from main import app

# Создаём тестовый клиент для FastAPI
client = TestClient(app)


def test_read_root():
    """Тест главной страницы"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello LOL"}


def test_health_check():
    """Тест для проверки работоспособности"""
    response = client.get("/")
    assert response.status_code == 200


def test_response_type():
    """Тест типа ответа"""
    response = client.get("/")
    assert isinstance(response.json(), dict)
    assert "message" in response.json()


def test_not_found():
    """Тест обработки несуществующего маршрута"""
    response = client.get("/nonexistent")
    assert response.status_code == 404