import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app_dir = os.path.abspath(os.path.dirname(__file__))
db_name = 'sqlite2.db'


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(app_dir, db_name)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
app.app_context().push()


class UserModel(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    login = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(100), unique=False, nullable=False)

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.name, self.email, self.login)


db.create_all()

for user in UserModel.query.all():
    db.session.delete(user)
db.session.commit()

userName = 'userName'
userLogin = 'userLogin'
userEmail = 'userEmail'
userPassword = 'userPassword'

newUser = UserModel(
    name=userName,
    login=userLogin,
    email=userEmail,
    password_hash=userPassword)

db.session.add(newUser)
db.session.commit()


@app.route('/')
def home_page():
    return "<html><title>TEST</title></html>"


@app.route('/about')
def about_page():
    return "<html><title>about</title><body>about</body></html>"


if __name__ == '__main__':

    app.run(debug=True)
