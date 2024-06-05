from main import UserModel, ClientModel
from werkzeug.security import generate_password_hash, check_password_hash


def test_new_user():

    userName = 'name'
    userLogin = 'login'
    userEmail = 'email'
    userPassword = 'password'

    newUser = UserModel(
        name=userName,
        login=userLogin,
        email=userEmail,
        password_hash=generate_password_hash(userPassword))

    assert newUser.name == userName
    assert newUser.login == userLogin
    assert newUser.email == userEmail
    assert check_password_hash(newUser.password_hash, userPassword) == True


def test_new_client():

    clientName = 'name'
    clientLogin = 'login'
    clientEmail = 'email'
    clientPassword = 'password'

    newClient = ClientModel(
        name=clientName,
        login=clientLogin,
        email=clientEmail,
        password_hash=generate_password_hash(clientPassword))

    assert newClient.name == clientName
    assert newClient.login == clientLogin
    assert newClient.email == clientEmail
    assert check_password_hash(newClient.password_hash, clientPassword) == True
