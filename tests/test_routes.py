
import io
from main import CategoryModel, ClientModel, PositionModel, app, db
from main import UserModel


# Тестирование маршрутов пользователя

def test_user_routes():
    # Задаем имя пользователя
    userName = 'userName'
    # Задаем логин пользователя
    userLogin = 'userLogin'
    # Задаем email пользователя
    userEmail = 'userEmail'
    # Задаем пароль пользователя
    userPassword = 'userPassword'

    # Инициализируем тестового клиента
    with app.test_client() as client:
        # Отправляем POST запрос на добавление нового пользователя
        client.post(
            '/add_new_user',
            data={
                "name": userName,
                "login": userLogin,
                "email": userEmail,
                "password": userPassword
            }
        )

        # Проверяем, что пользователь с заданным именем существует в базе данных
        assert UserModel.query.filter_by(name=userName).first() != None

    # Отправляем GET запрос на получение списка пользователей
    response = app.test_client().get('/users_list')
    # Проверяем, что имя пользователя присутствует в ответе
    assert userName in response.get_data(as_text=True)

    # Получаем объект пользователя из базы данных
    testUser = UserModel.query.filter_by(name=userName).first()
    # Удаляем пользователя из базы данных
    db.session.delete(testUser)
    # Подтверждаем изменения в базе данных
    db.session.commit()


# Тестирование маршрутов клиента

def test_client_routes():
    # Задаем имя клиента
    clientName = 'clientName'
    # Задаем логин клиента
    clientLogin = 'clientLogin'
    # Задаем email клиента
    clientEmail = 'clientEmail'
    # Задаем пароль клиента
    clientPassword = 'clientPassword'

    # Инициализируем тестового клиента
    with app.test_client() as client:
        # Отправляем POST запрос на добавление нового клиента
        client.post(
            '/add_new_client',
            data={
                "name": clientName,
                "login": clientLogin,
                "email": clientEmail,
                "password": clientPassword
            }
        )

        # Проверяем, что клиент с заданным именем существует в базе данных
        assert ClientModel.query.filter_by(name=clientName).first() != None

    # Отправляем GET запрос на получение списка клиентов
    response = app.test_client().get('/clients_list')
    # Проверяем, что имя клиента присутствует в ответе
    assert clientName in response.get_data(as_text=True)

    # Получаем объект клиента из базы данных
    testClient = ClientModel.query.filter_by(name=clientName).first()
    # Удаляем клиента из базы данных
    db.session.delete(testClient)
    # Подтверждаем изменения в базе данных
    db.session.commit()

# Тестирование маршрутов категории


def test_category_routes():
    # Задаем имя категории
    categoryName = 'categoryName'
    # Задаем описание категории
    categoryDiscription = 'categoryDiscription'
    # Задаем файл категории
    categoryFile = (io.BytesIO(b"TEST"), 'test.jpg')

    # Инициализируем тестового клиента
    with app.test_client() as client:
        # Отправляем POST запрос на добавление новой категории
        client.post(
            '/add_new_category',
            data={
                "name": categoryName,
                "discription": categoryDiscription,
                "file": categoryFile
            }
        )

        # Проверяем, что категория с заданным именем существует в базе данных
        assert CategoryModel.query.filter_by(name=categoryName).first() != None

    # Отправляем GET запрос на получение категорий
    response = app.test_client().get('/categories')
    # Проверяем, что имя категории присутствует в ответе
    assert categoryName in response.get_data(as_text=True)

    # Отправляем GET запрос на получение списка категорий
    response = app.test_client().get('/categories_list')
    # Проверяем, что имя категории присутствует в ответе
    assert categoryName in response.get_data(as_text=True)

    # Получаем объект категории из базы данных
    testCategory = CategoryModel.query.filter_by(name=categoryName).first()
    # Удаляем категорию из базы данных
    db.session.delete(testCategory)
    # Подтверждаем изменения в базе данных
    db.session.commit()


# Определение функции для тестирования маршрутов позиций
def test_positiont_routes():

    # Установка имени позиции
    positionName = 'positionName'
    # Установка описания позиции
    positionDiscription = 'positionDiscription'
    # Установка цены позиции
    positionPrice = "999"
    # Установка ID категории позиции
    positionCategoryId = "1"
    # Создание файла изображения для позиции
    imagesFile = (io.BytesIO(b"TEST"), 'test.jpg')

    # Создание тестового клиента приложения
    with app.test_client() as client:
        # Отправка POST-запроса на добавление новой позиции с указанными данными
        client.post(
            '/add_new_position',
            data={
                "name": positionName,
                "discription": positionDiscription,
                "price": positionPrice,
                "category_id": positionCategoryId,
                "file": imagesFile
            }
        )

        # Проверка, что позиция с указанным именем была добавлена в базу данных
        assert PositionModel.query.filter_by(name=positionName).first() != None

    # Отправка GET-запроса на получение позиций в категории с ID 1 и проверка, что имя позиции присутствует в ответе
    response = app.test_client().get('/category/1')
    assert positionName in response.get_data(as_text=True)

    # Отправка GET-запроса на получение списка всех позиций и проверка, что имя позиции присутствует в ответе
    response = app.test_client().get('/positions_list')
    assert positionName in response.get_data(as_text=True)

    # Получение тестовой позиции из базы данных
    testPosition = PositionModel.query.filter_by(name=positionName).first()
    # Удаление тестовой позиции из базы данных
    db.session.delete(testPosition)
    # Применение изменений в базе данных
    db.session.commit()
