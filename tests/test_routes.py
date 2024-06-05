
import io
from main import CategoryModel, ClientModel, PositionModel, app, db
from main import UserModel


def test_user_routes():

    userName = 'userName'
    userLogin = 'userLogin'
    userEmail = 'userEmail'
    userPassword = 'userPassword'

    with app.test_client() as client:
        client.post(
            '/add_new_user',
            data={
                "name": userName,
                "login": userLogin,
                "email": userEmail,
                "password": userPassword
            }
        )

        assert UserModel.query.filter_by(name=userName).first() != None

    response = app.test_client().get('/users_list')
    assert userName in response.get_data(as_text=True)

    testUser = UserModel.query.filter_by(name=userName).first()
    db.session.delete(testUser)
    db.session.commit()


def test_client_routes():

    clientName = 'clientName'
    clientLogin = 'clientLogin'
    clientEmail = 'clientEmail'
    clientPassword = 'clientPassword'

    with app.test_client() as client:
        client.post(
            '/add_new_client',
            data={
                "name": clientName,
                "login": clientLogin,
                "email": clientEmail,
                "password": clientPassword
            }
        )

        assert ClientModel.query.filter_by(name=clientName).first() != None

    response = app.test_client().get('/clients_list')
    assert clientName in response.get_data(as_text=True)

    testClient = ClientModel.query.filter_by(name=clientName).first()
    db.session.delete(testClient)
    db.session.commit()


def test_category_routes():

    categoryName = 'categoryName'
    categoryDiscription = 'categoryDiscription'
    categoryFile = (io.BytesIO(b"TEST"), 'test.jpg')

    with app.test_client() as client:
        client.post(
            '/add_new_category',
            data={
                "name": categoryName,
                "discription": categoryDiscription,
                "file": categoryFile
            }
        )

        assert CategoryModel.query.filter_by(name=categoryName).first() != None

    response = app.test_client().get('/categories')
    assert categoryName in response.get_data(as_text=True)

    response = app.test_client().get('/categories_list')
    assert categoryName in response.get_data(as_text=True)

    testCategory = CategoryModel.query.filter_by(name=categoryName).first()
    db.session.delete(testCategory)
    db.session.commit()


def test_positiont_routes():

    positionName = 'positionName'
    positionDiscription = 'positionDiscription'
    positionPrice = "999"
    positionCategoryId = "1"
    imagesFile = (io.BytesIO(b"TEST"), 'test.jpg')

    with app.test_client() as client:
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

        assert PositionModel.query.filter_by(name=positionName).first() != None

    response = app.test_client().get('/category/1')
    assert positionName in response.get_data(as_text=True)

    response = app.test_client().get('/positions_list')
    assert positionName in response.get_data(as_text=True)

    testPosition = PositionModel.query.filter_by(name=positionName).first()
    db.session.delete(testPosition)
    db.session.commit()
