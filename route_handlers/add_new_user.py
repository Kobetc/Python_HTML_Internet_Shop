from flask import redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

from werkzeug.security import generate_password_hash


def addNewUserHandler(UserModel, db: SQLAlchemy, autorization, basket):

    if request.method == 'POST':
        userName = request.form.get('name')
        userLogin = request.form.get('login')
        userEmail = request.form.get('email')
        userPassword = request.form.get('password')

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
            name=userName,
            login=userLogin,
            email=userEmail,
            password_hash=generate_password_hash(userPassword)
        )

        try:
            db.session.add(newUser)
            db.session.commit()

            return redirect('/')
        except:
            return 'ОШИБКА !!! При сохранении пользователя в базу.'
    else:
        return render_template('add_new_user.html', autorization=autorization, basket=basket)
