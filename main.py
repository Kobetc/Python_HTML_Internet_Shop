import os
import base64

from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

from werkzeug.security import generate_password_hash, check_password_hash

from models.image import createImageModel
from models.position import createPositionModel
from models.user import createUserModel
from route_handlers.images import images_handler

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

@app.route('/images', methods=['GET', 'POST'])
def images():
    return images_handler(ImageModel, db)


@app.route('/add_user', methods=[ 'POST', 'GET'])
def add_user_page():

    if request.method == 'POST':
        userName = request.form['name']
        userLogin = request.form['login']
        userEmail = request.form['email']
        userPassword = request.form['password']

        isUserNameExist = UserModel.query.filter_by(name=userName).first()
        isUserLoginExist = UserModel.query.filter_by(login=userLogin).first()
        isUserEmailExist = UserModel.query.filter_by(email=userEmail).first()

        if (isUserNameExist != None):
            return 'ОШИБКА !!! Пользователь с таким именем существует.'
        if (isUserLoginExist != None):
            return 'ОШИБКА !!! Пользователь с таким логином существует.'
        if (isUserEmailExist != None):
            return 'ОШИБКА !!! Пользователь с таким адресом почты существует.'

        newUser = UserModel(
            name = userName,
            login = userLogin,
            email = userEmail,
            password_hash = generate_password_hash(userPassword)
        )

        try:
            db.session.add(newUser)
            db.session.commit()

            return redirect('/')
        except:
            return 'ОШИБКА !!! При сохранении пользователя в базу.'
    else:
        return render_template('add_user.html')
    
@app.route('/add_images', methods=[ 'POST', 'GET'])
def add_images_page():
    if request.method == 'POST':
        file = request.files['uploadImage']

        isFileNameExist = ImageModel.query.filter_by(name=file.filename).first()

        if (isFileNameExist != None):
            return render_template('add_images.html')

        fileData = file.read()

        newImage = ImageModel(
            name = file.filename,
            data = fileData,
            position_id = 1
        )

        try:
            db.session.add(newImage)
        except:
            return 'ОШИБКА !!! При сохранении изображения в базу.'
            
        db.session.commit()

    return render_template('add_images.html')
    

if __name__ == '__main__':
    app.run(debug = True)