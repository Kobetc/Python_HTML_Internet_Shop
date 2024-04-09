import os
from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

from werkzeug.security import generate_password_hash, check_password_hash

from autorization import Autorization
from models.client import createClientModel
from models.image import createImageModel
from models.position import createPositionModel
from models.user import createUserModel
from route_handlers.add_new_client import addNewClientHandler
from route_handlers.add_new_position import addNewPositionHandler
from route_handlers.add_new_user import addNewUserHandler
from route_handlers.client_login import clientLoginHandler
from route_handlers.clients_list import clientsListHandler
from route_handlers.positions_images_list import positionsImagesListHandler
from route_handlers.positions_list import positionsListHandler
from route_handlers.user_login import userLoginHandler
from route_handlers.users_list import usersListHandler

app_dir = os.path.abspath(os.path.dirname(__file__))
db_name = 'sqlite.db'

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app_dir, db_name)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.app_context().push()

autorization = Autorization() 

###
### DB Models ###
###

ImageModel = createImageModel(db)
PositionModel = createPositionModel(db)
UserModel = createUserModel(db)
ClientModel = createClientModel(db)

###
### Routes ###
###

@app.route('/')
def home_page():
    return render_template('index.html', isUserLogin=autorization.isUserLogin, isClientLogin=autorization.isClientLogin)

@app.route('/about')
def about_page():
    return render_template('about.html', isUserLogin=autorization.isUserLogin, isClientLogin=autorization.isClientLogin)


#
# Добавление новой позиции
#

@app.route('/add_new_position', methods=[ 'POST', 'GET'])
def addNewPosition():
    return  addNewPositionHandler(PositionModel, ImageModel, db, autorization)

#
# Список изображений всех позиций
#

@app.route('/positions_images_list', methods=[ 'POST', 'GET'])
def positionsImagesList():
    return  positionsImagesListHandler(ImageModel, PositionModel, db, autorization)

#
# Список всех позиций
#

@app.route('/positions_list', methods=[ 'POST', 'GET'])
def positionsList():
    return  positionsListHandler(PositionModel, ImageModel, db, autorization)

#
# Разлогин пользователя или покупателя
#

@app.route('/logout')
def unlogin():

    autorization.logout()

    return redirect('/')

#
# Добавление нового администратора
#

@app.route('/add_new_user', methods=[ 'POST', 'GET'])
def addNewUser():
    return addNewUserHandler(UserModel, db, autorization)
    


#
# Вход администратора
#

@app.route('/user_login', methods=[ 'POST', 'GET'])
def userLogin():
    return  userLoginHandler(UserModel, autorization)

#
# Список администраторов
#

@app.route('/users_list', methods=[ 'POST', 'GET'])
def usersList():
    return  usersListHandler(UserModel, db, autorization)

#
# Добавление нового клиента
#

@app.route('/add_new_client', methods=[ 'POST', 'GET'])
def addNewClient():
    return addNewClientHandler(ClientModel, db, autorization)
    

#
# Вход клиента
#

@app.route('/client_login', methods=[ 'POST', 'GET'])
def clientLogin():
    return  clientLoginHandler(ClientModel, autorization)

#
# Список клиентов
#

@app.route('/clients_list', methods=[ 'POST', 'GET'])
def clientsList():
    return  clientsListHandler(ClientModel, db, autorization)

if __name__ == '__main__':

    app.run(debug = True)