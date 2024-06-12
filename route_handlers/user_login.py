from flask import redirect, render_template, request

from werkzeug.security import check_password_hash


# Определяем функцию обработчика входа пользователя
def userLoginHandler(UserModel, autorization, basket):

    # Проверяем, является ли метод запроса POST
    if request.method == 'POST':

        # Получаем логин пользователя из формы
        userLogin = request.form.get('login')

        # Получаем пароль пользователя из формы
        userPassword = request.form.get('password')

        # Проверяем, существует ли такой логин в базе данных
        isUserLoginExist = UserModel.query.filter_by(login=userLogin).first()

        # Если такой логин существует
        if isUserLoginExist != None:

            # Проверяем, верный ли пароль
            isPassworValid = check_password_hash(
                isUserLoginExist.password_hash, userPassword)

            # Если пароль верный
            if isPassworValid == True:

                # Авторизуем пользователя
                autorization.loginUser(isUserLoginExist.name)

                # Перенаправляем пользователя на главную страницу
                return redirect('/')

    # Возвращаем шаблон страницы входа
    return render_template('user_login.html', autorization=autorization, basket=basket)
