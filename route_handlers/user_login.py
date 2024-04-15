from flask import redirect, render_template, request

from werkzeug.security import check_password_hash


def userLoginHandler(UserModel, autorization, basket):

    if request.method == 'POST':
        userLogin = request.form.get('login')
        userPassword = request.form.get('password')

        isUserLoginExist = UserModel.query.filter_by(login=userLogin).first()

        if isUserLoginExist != None:
            isPassworValid = check_password_hash(
                isUserLoginExist.password_hash, userPassword)

            if isPassworValid == True:
                autorization.loginUser(isUserLoginExist.name)

                return redirect('/')

    return render_template('user_login.html', autorization=autorization, basket=basket)
