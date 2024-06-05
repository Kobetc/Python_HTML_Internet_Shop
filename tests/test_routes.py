
from main import ClientModel, app
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
