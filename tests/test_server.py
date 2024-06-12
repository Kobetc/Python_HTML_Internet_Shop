from main import app


# Тестирование ответа веб-сервера
def test_web_server_responce_code():
    # Отправка GET запроса на главную страницу
    response = app.test_client().get('/')
    # Проверка, что статус ответа равен 200 (успешно)
    assert response.status_code == 200

# Тестирование главной страницы


def test_main_page():
    # Отправка GET запроса на главную страницу
    response = app.test_client().get('/')
    # Проверка, что в ответе присутствует нужный HTML тег
    assert "<title>Интернет-магазин - Главная страница</title>" in response.get_data(
        as_text=True)

# Тестирование страницы категорий


def test_categories_page():
    # Отправка GET запроса на страницу категорий
    response = app.test_client().get('/categories')
    # Проверка, что в ответе присутствует нужный HTML тег
    assert "<title>Интернет-магазин - Просмотр списка категорий</title>" in response.get_data(
        as_text=True)

# Тестирование страницы конкретной категории


def test_category_1_page():
    # Отправка GET запроса на страницу конкретной категории
    response = app.test_client().get('/category/1')
    # Проверка, что в ответе присутствует нужный HTML тег
    assert "<title>Интернет-магазин - Просмотр списка позиций в категории</title>" in response.get_data(
        as_text=True)

# Тестирование страницы "О сайте"


def test_about_page():
    # Отправка GET запроса на страницу "О сайте"
    response = app.test_client().get('/about')
    # Проверка, что в ответе присутствует нужный HTML тег
    assert "<title>Интернет-магазин - О сайте</title>" in response.get_data(
        as_text=True)

# Тестирование страницы входа клиента


def test_client_login_page():
    # Отправка GET запроса на страницу входа клиента
    response = app.test_client().get('/client_login')
    # Проверка, что в ответе присутствует нужный HTML тег
    assert "<title>Интернет-магазин - Вход клиента</title>" in response.get_data(
        as_text=True)

# Тестирование страницы входа администратора


def test_user_login_page():
    # Отправка GET запроса на страницу входа администратора
    response = app.test_client().get('/user_login')
    # Проверка, что в ответе присутствует нужный HTML тег
    assert "<title>Интернет-магазин - Вход администратора</title>" in response.get_data(
        as_text=True)
