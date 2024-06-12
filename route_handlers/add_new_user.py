from flask import redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

from werkzeug.security import generate_password_hash


def addNewUserHandler(UserModel, db: SQLAlchemy, autorization, basket):

    # Проверяем, является ли метод запроса POST
    if request.method == 'POST':
        # Получаем имя пользователя из формы
        userName = request.form.get('name')
        # Получаем логин пользователя из формы
        userLogin = request.form.get('login')
        # Получаем адрес электронной почты пользователя из формы
        userEmail = request.form.get('email')
        # Получаем пароль пользователя из формы
        userPassword = request.form.get('password')

        # Проверяем, существует ли уже пользователь с таким именем
        isUserNameExist = UserModel.query.filter_by(name=userName).first()
        # Проверяем, существует ли уже пользователь с таким логином
        isUserLoginExist = UserModel.query.filter_by(login=userLogin).first()
        # Проверяем, существует ли уже пользователь с таким адресом электронной почты
        isUserEmailExist = UserModel.query.filter_by(email=userEmail).first()

        # Если пользователь с таким именем уже существует, возвращаем сообщение об ошибке
        if (isUserNameExist != None):
            return 'ОШИБКА !!! Пользователь с таким именем существует.'
        # Если пользователь с таким логином уже существует, возвращаем сообщение об ошибке
        if (isUserLoginExist != None):
            return 'ОШИБКА !!! Пользователь с таким логином существует.'
        # Если пользователь с таким адресом электронной почты уже существует, возвращаем сообщение об ошибке
        if (isUserEmailExist != None):
            return 'ОШИБКА !!! Пользователь с таким адресом почты существует.'

        # Создаем нового пользователя
        newUser = UserModel(
            name=userName,
            login=userLogin,
            email=userEmail,
            password_hash=generate_password_hash(userPassword)
        )

        # Пытаемся добавить нового пользователя в базу данных
        try:
            db.session.add(newUser)
            db.session.commit()

            # После успешного добавления пользователя в базу данных, перенаправляем пользователя на главную страницу
            return redirect('/')
        except:
            # Если при сохранении пользователя в базу данных произошла ошибка, возвращаем сообщение об ошибке
            return 'ОШИБКА !!! При сохранении пользователя в базу.'
    else:
        # Если метод запроса не POST, возвращаем HTML-шаблон для добавления нового пользователя
        return render_template('add_new_user.html', autorization=autorization, basket=basket)
