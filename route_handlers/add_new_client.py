from flask import redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

from werkzeug.security import generate_password_hash, check_password_hash


def addNewClientHandler(ClientModel, db: SQLAlchemy, autorization):

    if request.method == 'POST':
        clientName = request.form['name']
        clientLogin = request.form['login']
        clientEmail = request.form['email']
        clientPassword = request.form['password']

        isClientNameExist = ClientModel.query.filter_by(name=clientName).first()
        isClientLoginExist = ClientModel.query.filter_by(login=clientLogin).first()
        isClientEmailExist = ClientModel.query.filter_by(email=clientEmail).first()

        if (isClientNameExist != None):
            return 'ОШИБКА !!! Клиент с таким именем существует.'
        if (isClientLoginExist != None):
            return 'ОШИБКА !!! Клиент с таким логином существует.'
        if (isClientEmailExist != None):
            return 'ОШИБКА !!! Клиент с таким адресом почты существует.'

        newClient = ClientModel(
            name = clientName,
            login = clientLogin,
            email = clientEmail,
            password_hash = generate_password_hash(clientPassword)
        )

        try:
            db.session.add(newClient)
            db.session.commit()

            return redirect('/')
        except:
            return 'ОШИБКА !!! При сохранении клиента в базу.'
    else:
        return render_template('add_new_user.html', isUserLogin=autorization.isUserLogin, isClientLogin=autorization.isClientLogin)