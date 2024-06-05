# test_main.py
from main import app


def test_web_server_responce_code():
    response = app.test_client().get('/')

    assert response.status_code == 200


def test_main_page():
    response = app.test_client().get('/')

    assert "<title>Интернет-магазин - Главная страница</title>" in response.get_data(
        as_text=True)
