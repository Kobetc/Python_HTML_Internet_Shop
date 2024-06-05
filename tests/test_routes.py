
import io
from main import CategoryModel, ClientModel, PositionModel, app, db
from main import UserModel


def test_add_new_user_route():

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

    testUser = UserModel.query.filter_by(name=userName).first()
    db.session.delete(testUser)
    db.session.commit()


def test_add_new_client_route():

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

    testClient = ClientModel.query.filter_by(name=clientName).first()
    db.session.delete(testClient)
    db.session.commit()


def test_add_new_category_route():

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

    testCategory = CategoryModel.query.filter_by(name=categoryName).first()
    db.session.delete(testCategory)
    db.session.commit()


def test_add_new_positiont_route():

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

    testPosition = PositionModel.query.filter_by(name=positionName).first()
    db.session.delete(testPosition)
    db.session.commit()
