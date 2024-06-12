from flask import redirect, render_template, request

from werkzeug.security import check_password_hash


# Определяем функцию clientLoginHandler, которая принимает три параметра: ClientModel, autorization и basket
def clientLoginHandler(ClientModel, autorization, basket):

    # Проверяем, является ли метод запроса POST
    if request.method == 'POST':
        # Получаем значение 'login' из формы
        userLogin = request.form.get('login')
        # Получаем значение 'password' из формы
        userPassword = request.form.get('password')

        # Проверяем, существует ли клиент с таким логином в базе данных
        isClientLoginExist = ClientModel.query.filter_by(
            login=userLogin).first()

        # Если клиент с таким логином существует
        if isClientLoginExist != None:
            # Проверяем, верен ли введенный пароль
            isPassworValid = check_password_hash(
                isClientLoginExist.password_hash, userPassword)

            # Если пароль верен
            if isPassworValid == True:
                # Авторизуем клиента
                autorization.loginClient(isClientLoginExist.name)

                # Перенаправляем на главную страницу
                return redirect('/')

    # Если метод запроса не POST, то отображаем страницу входа
    return render_template('client_login.html', autorization=autorization, basket=basket)
