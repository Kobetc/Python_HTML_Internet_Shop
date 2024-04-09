import os
import base64

from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

from werkzeug.security import generate_password_hash, check_password_hash

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
class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100))
    login = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.name, self.email, self.login)
    
class PositionModel(db.Model):
    __tablename__ = 'positions'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), unique=True)
    discription = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.name)
    
class ImageModel(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), unique=True)
    data = db.Column(db.BLOB, nullable=False)
    position_id = db.Column(db.Integer())

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.name)

###
### Routes ###
###
    
@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/images')
def images_page():
    imagesFromQuery = ImageModel.query.filter_by(position_id=1).all()
    images = [ base64.b64encode(image.data).decode('ascii') for image in imagesFromQuery ]

    return render_template('images.html', images=images)

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