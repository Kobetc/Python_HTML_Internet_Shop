import os
import base64

from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

from werkzeug.security import generate_password_hash, check_password_hash

from models.image import createImageModel
from models.position import createPositionModel
from models.user import createUserModel
from route_handlers.add_new_position import addNewPositionHandler
from route_handlers.add_new_user import addNewUserHandler
from route_handlers.positions_images_list import positionsImagesListHandler
from route_handlers.positions_list import positionsListHandler


app_dir = os.path.abspath(os.path.dirname(__file__))
db_name = 'sqlite.db'

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app_dir, db_name)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.app_context().push()

###
### DB Models ###
###

ImageModel = createImageModel(db)
UserModel = createUserModel(db)
PositionModel = createPositionModel(db)

###
### Routes ###
###

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

#
# Добавление нового пользователя
#

@app.route('/add_new_user', methods=[ 'POST', 'GET'])
def addNewUser():
    return addNewUserHandler(UserModel, db)
    

#
# Добавление новой позиции
#

@app.route('/add_new_position', methods=[ 'POST', 'GET'])
def addNewPosition():
    return  addNewPositionHandler(PositionModel, ImageModel, db)

#
# Список изображений всех позиций
#

@app.route('/positions_images_list', methods=[ 'POST', 'GET'])
def positionsImagesList():
    return  positionsImagesListHandler(ImageModel, PositionModel, db)

#
# Список всех позиций
#

@app.route('/positions_list', methods=[ 'POST', 'GET'])
def positionsList():
    return  positionsListHandler(PositionModel, ImageModel, db)

if __name__ == '__main__':

    app.run(debug = True)