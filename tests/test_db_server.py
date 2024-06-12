from main import CategoryModel, ClientModel, ImageModel, PositionModel, UserModel


# Тестовая функция для проверки списка клиентов из базы данных
def test_client_list_from_db():
    # Получение всех клиентов из базы данных
    ClientsFromQuery = ClientModel.query.all()

    # Проверка, что полученный список клиентов не равен None
    assert ClientsFromQuery != None


# Тестовая функция для проверки списка пользователей из базы данных
def test_user_list_from_db():
    # Получение всех пользователей из базы данных
    UsersFromQuery = UserModel.query.all()

    # Проверка, что полученный список пользователей не равен None
    assert UsersFromQuery != None


# Тестовая функция для проверки списка категорий из базы данных
def test_category_list_from_db():
    # Получение всех категорий из базы данных
    CategoriesFromQuery = CategoryModel.query.all()

    # Проверка, что полученный список категорий не равен None
    assert CategoriesFromQuery != None


# Тестовая функция для проверки списка позиций из базы данных
def test_position_list_from_db():
    # Получение всех позиций из базы данных
    PositionsFromQuery = PositionModel.query.all()

    # Проверка, что полученный список позиций не равен None
    assert PositionsFromQuery != None


# Тестовая функция для проверки списка изображений из базы данных
def test_image_list_from_db():
    # Получение всех изображений из базы данных
    ImagesFromQuery = ImageModel.query.all()

    # Проверка, что полученный список изображений не равен None
    assert ImagesFromQuery != None
