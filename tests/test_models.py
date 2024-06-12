from sqlite3 import Blob


from basket import Basket
from main import CategoryModel, ImageModel, PositionModel, UserModel, ClientModel, db
from werkzeug.security import generate_password_hash, check_password_hash


# Тестовая функция для проверки модели пользователя
def test_user_model():
    # Задаем тестовые данные для пользователя
    userName = 'userName'
    userLogin = 'userLogin'
    userEmail = 'userEmail'
    userPassword = 'userPassword'

    # Создаем нового пользователя с использованием тестовых данных
    newUser = UserModel(
        name=userName,
        login=userLogin,
        email=userEmail,
        password_hash=generate_password_hash(userPassword))

    # Проверка, что данные пользователя соответствуют заданным тестовым данным
    assert newUser.name == userName
    assert newUser.login == userLogin
    assert newUser.email == userEmail
    # Проверка, что хэш пароля соответствует заданному тестовому паролю
    assert check_password_hash(newUser.password_hash, userPassword) == True


# Тестовая функция для проверки модели клиента
def test_client_model():
    # Задаем тестовые данные для клиента
    clientName = 'clientName'
    clientLogin = 'clientLogin'
    clientEmail = 'clientEmail'
    clientPassword = 'clientPassword'

    # Создаем нового клиента с использованием тестовых данных
    newClient = ClientModel(
        name=clientName,
        login=clientLogin,
        email=clientEmail,
        password_hash=generate_password_hash(clientPassword))

    # Проверка, что данные клиента соответствуют заданным тестовым данным
    assert newClient.name == clientName
    assert newClient.login == clientLogin
    assert newClient.email == clientEmail
    # Проверка, что хэш пароля соответствует заданному тестовому паролю
    assert check_password_hash(newClient.password_hash, clientPassword) == True


# Тестовая функция для проверки модели категории
def test_category_model():
    # Задаем тестовые данные для категории
    categoryName = 'categoryName'
    categoryDiscription = 'categoryDiscription'
    categoryImage = b'TEST'

    # Создаем новую категорию с использованием тестовых данных
    newCategory = CategoryModel(
        name=categoryName,
        discription=categoryDiscription,
        image=categoryImage)

    # Проверка, что данные категории соответствуют заданным тестовым данным
    assert newCategory.name == categoryName
    assert newCategory.discription == categoryDiscription


# Тестовая функция для проверки модели позиции
def test_position_model():
    # Задаем тестовые данные для позиции
    positionName = 'positionName'
    positionDiscription = 'positionDiscription'
    positionPrice = 1
    positionCategoryId = 1

    # Создаем новую позицию с использованием тестовых данных
    newPosition = PositionModel(
        name=positionName,
        discription=positionDiscription,
        price=positionPrice,
        category_id=positionCategoryId)

    # Проверка, что данные позиции соответствуют заданным тестовым данным
    assert newPosition.name == positionName
    assert newPosition.discription == positionDiscription


# Тестовая функция для проверки модели изображения
def test_image_model():
    # Задаем тестовые данные для изображения
    imageName = 'imageName'
    imageData = b'TEST'
    imagePositionId = 1

    # Создаем новое изображение с использованием тестовых данных
    newImage = ImageModel(
        name=imageName,
        data=imageData,
        position_id=imagePositionId)

    # Проверка, что данные изображения соответствуют заданным тестовым данным
    assert newImage.name == imageName


# Тестовая функция для проверки модели корзины
def test_basket_model():
    # Задаем тестовые данные для позиции
    positionName = 'positionName'
    positionDiscription = 'positionDiscription'
    positionPrice = 999
    positionCategoryId = 1

    # Создаем две новые позиции с использованием тестовых данных
    position1 = PositionModel(
        id=1,
        name=positionName,
        discription=positionDiscription,
        price=positionPrice,
        category_id=positionCategoryId)

    position2 = PositionModel(
        id=2,
        name=positionName,
        discription=positionDiscription,
        price=positionPrice,
        category_id=positionCategoryId)

    # Создаем новую корзину
    basket = Basket()

    # Добавляем позиции в корзину
    basket.addPositionToBasket(position1)
    basket.addPositionToBasket(position2)

    # Проверка, что в корзине две позиции и общая стоимость корзины равна удвоенной стоимости позиции
    assert basket.basketLen == 2
    assert basket.basketPrice == positionPrice * 2
    # Проверка, что количество позиции с id=1 в корзине равно 1
    assert basket.basket["1"]["count"] == 1

    # Увеличиваем количество позиции с id=1 в корзине на 1
    basket.plusPositionToBasket(1)
    # Проверка, что количество позиции с id=1 в корзине стало равно 2
    assert basket.basket["1"]["count"] == 2

    # Удаляем позицию с id=2 из корзины
    basket.clearBasketPosition(2)
    # Проверка, что в корзине осталась одна позиция
    assert basket.basketLen == 1
