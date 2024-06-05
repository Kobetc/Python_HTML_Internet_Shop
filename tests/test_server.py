from main import app

# Проверка доступности WEB сервера


def test_web_server_responce_code():
    response = app.test_client().get('/')

    assert response.status_code == 200

# Проверка доступности главной страницы


def test_main_page():
    response = app.test_client().get('/')

    assert "<title>Интернет-магазин - Главная страница</title>" in response.get_data(
        as_text=True)

# Проверка доступности страницы категорий


def test_categories_page():
    response = app.test_client().get('/categories')

    assert "<title>Интернет-магазин - Просмотр списка категорий</title>" in response.get_data(
        as_text=True)

# Проверка доступности списка позиций категории с id = 1


def test_category_1_page():
    response = app.test_client().get('/category/1')

    assert "<title>Интернет-магазин - Просмотр списка позиций в категории</title>" in response.get_data(
        as_text=True)

# Проверка доступности страницы описания сайта


def test_about_page():
    response = app.test_client().get('/about')

    assert "<title>Интернет-магазин - О сайте</title>" in response.get_data(
        as_text=True)
