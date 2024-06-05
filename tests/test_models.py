from sqlite3 import Blob


from basket import Basket
from main import CategoryModel, ImageModel, PositionModel, UserModel, ClientModel, db
from werkzeug.security import generate_password_hash, check_password_hash


def test_user_model():

    userName = 'userName'
    userLogin = 'userLogin'
    userEmail = 'userEmail'
    userPassword = 'userPassword'

    newUser = UserModel(
        name=userName,
        login=userLogin,
        email=userEmail,
        password_hash=generate_password_hash(userPassword))

    assert newUser.name == userName
    assert newUser.login == userLogin
    assert newUser.email == userEmail
    assert check_password_hash(newUser.password_hash, userPassword) == True


def test_client_model():

    clientName = 'clientName'
    clientLogin = 'clientLogin'
    clientEmail = 'clientEmail'
    clientPassword = 'clientPassword'

    newClient = ClientModel(
        name=clientName,
        login=clientLogin,
        email=clientEmail,
        password_hash=generate_password_hash(clientPassword))

    assert newClient.name == clientName
    assert newClient.login == clientLogin
    assert newClient.email == clientEmail
    assert check_password_hash(newClient.password_hash, clientPassword) == True


def test_category_model():

    categoryName = 'categoryName'
    categoryDiscription = 'categoryDiscription'
    categoryImage = b'TEST'

    newCategory = CategoryModel(
        name=categoryName,
        discription=categoryDiscription,
        image=categoryImage)

    assert newCategory.name == categoryName
    assert newCategory.discription == categoryDiscription


def test_position_model():

    positionName = 'positionName'
    positionDiscription = 'positionDiscription'
    positionPrice = 1
    positionCategoryId = 1

    newPosition = PositionModel(
        name=positionName,
        discription=positionDiscription,
        price=positionPrice,
        category_id=positionCategoryId)

    assert newPosition.name == positionName
    assert newPosition.discription == positionDiscription


def test_image_model():

    imageName = 'imageName'
    imageData = b'TEST'
    imagePositionId = 1

    newImage = ImageModel(
        name=imageName,
        data=imageData,
        position_id=imagePositionId)

    assert newImage.name == imageName


def test_basket_model():

    positionName = 'positionName'
    positionDiscription = 'positionDiscription'
    positionPrice = 999
    positionCategoryId = 1

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

    basket = Basket()

    basket.addPositionToBasket(position1)
    basket.addPositionToBasket(position2)

    assert basket.basketLen == 2
    assert basket.basketPrice == positionPrice * 2
    assert basket.basket["1"]["count"] == 1

    basket.plusPositionToBasket(1)
    assert basket.basket["1"]["count"] == 2

    basket.clearBasketPosition(2)
    assert basket.basketLen == 1
