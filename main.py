import base64
import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app_dir = os.path.abspath(os.path.dirname(__file__))
db_name = 'sqlite.db'

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app_dir, db_name)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.app_context().push()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100))
    login = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.name, self.email, self.login)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,  password: str):
        return check_password_hash(self.password_hash, password)
    
class Position(db.Model):
    __tablename__ = 'positions'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), unique=True)
    discription = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.name)
    
class Image(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), unique=True)
    data = db.Column(db.BLOB, nullable=False)
    position_id = db.Column(db.Integer())

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.name)


@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/image')
def image_page():
    file_data = Image.query.filter_by(position_id=1).first()
    image = base64.b64encode(file_data.data).decode('ascii')
    return render_template('image.html', image=image)

@app.route('/add_user', methods=[ 'POST', 'GET'])
def add_user_page():

    if request.method == 'POST':
        userName = request.form['name']
        userLogin = request.form['login']
        userEmail = request.form['email']
        userPassword = request.form['password']

        isUserNameExist = User.query.filter_by(name=userName).first()
        isUserLoginExist = User.query.filter_by(login=userLogin).first()
        isUserEmailExist = User.query.filter_by(email=userEmail).first()

        if (isUserNameExist != None):
            return 'ОШИБКА !!! Пользователь с таким именем существует.'
        if (isUserLoginExist != None):
            return 'ОШИБКА !!! Пользователь с таким логином существует.'
        if (isUserEmailExist != None):
            return 'ОШИБКА !!! Пользователь с таким адресом почты существует.'

        print(isUserNameExist, isUserLoginExist, isUserEmailExist)
        print(userName, userLogin, userEmail, userPassword)

        newUser = User(
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

if __name__ == '__main__':
    app.run(debug = True)