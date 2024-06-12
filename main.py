import os
from flask import Flask, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

from autorization import Autorization
from basket import Basket

from models.category import createCategoryModel
from models.client import createClientModel
from models.image import createImageModel
from models.position import createPositionModel
from models.user import createUserModel

from route_handlers.add_new_category import addNewCategoryHandler
from route_handlers.add_new_client import addNewClientHandler
from route_handlers.add_new_position import addNewPositionHandler
from route_handlers.add_new_user import addNewUserHandler
from route_handlers.cart import cartHandler
from route_handlers.categories import categoriesHandler
from route_handlers.categories_list import categoriesListHandler
from route_handlers.client_login import clientLoginHandler
from route_handlers.clients_list import clientsListHandler
from route_handlers.category import categoryHandler
from route_handlers.positions_images_list import positionsImagesListHandler
from route_handlers.positions_list import positionsListHandler
from route_handlers.user_login import userLoginHandler
from route_handlers.users_list import usersListHandler

app_dir = os.path.abspath(os.path.dirname(__file__))
db_name = 'sqlite.db'

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(app_dir, db_name)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.app_context().push()

###
### DB Models ###
###

CategoryModel = createCategoryModel(db)
ImageModel = createImageModel(db)
PositionModel = createPositionModel(db)
UserModel = createUserModel(db)
ClientModel = createClientModel(db)

for image in ImageModel.query.all():
    db.session.delete(image)

for user in UserModel.query.all():
    db.session.delete(user)

for client in ClientModel.query.all():
    db.session.delete(client)

db.session.commit()

###
### Авторизация ###
###

autorization = Autorization(UserModel)

###
### Корзина товаров ###
###

basket = Basket()

###
### Routes ###
###


@app.route('/')
def home_page():
    return render_template('index.html', autorization=autorization, basket=basket)


@app.route('/about')
def about_page():
    return render_template('about.html', autorization=autorization, basket=basket)

#
# Добавление новой категории
#


@app.route('/add_new_category', methods=['POST', 'GET'])
def addNewCategory():
    return addNewCategoryHandler(CategoryModel, db, autorization, basket)

#
# Список категорий
#


@app.route('/categories_list', methods=['POST', 'GET'])
def categoriesList():
    return categoriesListHandler(CategoryModel, db, autorization, basket)

#
# Добавление новой позиции
#


@app.route('/add_new_position', methods=['POST', 'GET'])
def addNewPosition():
    return addNewPositionHandler(PositionModel, ImageModel, CategoryModel, db, autorization, basket)

#
# Список изображений всех позиций
#


@app.route('/positions_images_list', methods=['POST', 'GET'])
def positionsImagesList():
    return positionsImagesListHandler(ImageModel, PositionModel, db, autorization, basket)

#
# Список всех позиций
#


@app.route('/positions_list', methods=['POST', 'GET'])
def positionsList():
    return positionsListHandler(PositionModel, ImageModel, CategoryModel, db, autorization, basket)

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


@app.route('/add_new_user', methods=['POST', 'GET'])
def addNewUser():
    return addNewUserHandler(UserModel, db, autorization, basket)


#
# Вход администратора
#

@app.route('/user_login', methods=['POST', 'GET'])
def userLogin():
    return userLoginHandler(UserModel, autorization, basket)

#
# Список администраторов
#


@app.route('/users_list', methods=['POST', 'GET'])
def usersList():
    return usersListHandler(UserModel, db, autorization, basket)

#
# Добавление нового клиента
#


@app.route('/add_new_client', methods=['POST', 'GET'])
def addNewClient():
    return addNewClientHandler(ClientModel, db, autorization, basket)


#
# Вход клиента
#

@app.route('/client_login', methods=['POST', 'GET'])
def clientLogin():
    return clientLoginHandler(ClientModel, autorization, basket)

#
# Список клиентов
#


@app.route('/clients_list', methods=['POST', 'GET'])
def clientsList():
    return clientsListHandler(ClientModel, db, autorization, basket)


#
# Список категорий товаров
#


@app.route('/categories', methods=['POST', 'GET'])
def categories():
    return categoriesHandler(CategoryModel, autorization, basket)

#
# Список товаров выбранной категории
#


@app.route('/category/<int:id>', methods=['POST', 'GET'])
def category(id: int):
    return categoryHandler(id, PositionModel, ImageModel, CategoryModel, autorization, basket)

#
# Корзина
#


@app.route('/cart', methods=['POST', 'GET'])
def cart():
    return cartHandler(autorization, basket)


if __name__ == '__main__':

    app.run(debug=True)
