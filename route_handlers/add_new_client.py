from flask import redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

from werkzeug.security import generate_password_hash


# Определяем функцию для обработки добавления нового клиента
def addNewClientHandler(ClientModel, db: SQLAlchemy, autorization, basket):

    # Проверяем, является ли метод запроса POST
    if request.method == 'POST':
        # Получаем имя клиента из формы
        clientName = request.form.get('name')
        # Получаем логин клиента из формы
        clientLogin = request.form.get('login')
        # Получаем адрес электронной почты клиента из формы
        clientEmail = request.form.get('email')
        # Получаем пароль клиента из формы
        clientPassword = request.form.get('password')

        # Проверяем, существует ли уже клиент с таким именем
        isClientNameExist = ClientModel.query.filter_by(
            name=clientName).first()
        # Проверяем, существует ли уже клиент с таким логином
        isClientLoginExist = ClientModel.query.filter_by(
            login=clientLogin).first()
        # Проверяем, существует ли уже клиент с таким адресом электронной почты
        isClientEmailExist = ClientModel.query.filter_by(
            email=clientEmail).first()

        # Если клиент с таким именем уже существует, возвращаем ошибку
        if (isClientNameExist != None):
            return 'ОШИБКА !!! Клиент с таким именем существует.'
        # Если клиент с таким логином уже существует, возвращаем ошибку
        if (isClientLoginExist != None):
            return 'ОШИБКА !!! Клиент с таким логином существует.'
        # Если клиент с таким адресом электронной почты уже существует, возвращаем ошибку
        if (isClientEmailExist != None):
            return 'ОШИБКА !!! Клиент с таким адресом почты существует.'

        # Создаем нового клиента
        newClient = ClientModel(
            name=clientName,
            login=clientLogin,
            email=clientEmail,
            # Генерируем хэш пароля
            password_hash=generate_password_hash(clientPassword)
        )

        # Пытаемся сохранить нового клиента в базе данных
        try:
            db.session.add(newClient)
            db.session.commit()

            # Если сохранение прошло успешно, перенаправляем пользователя на главную страницу
            return redirect('/')
        except:
            # Если при сохранении произошла ошибка, возвращаем сообщение об ошибке
            return 'ОШИБКА !!! При сохранении клиента в базу.'
    else:
        # Если метод запроса не POST, рендерим шаблон с формой добавления нового пользователя
        return render_template('add_new_user.html', autorization=autorization, basket=basket)
