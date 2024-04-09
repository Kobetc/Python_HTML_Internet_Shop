from flask import redirect, render_template, request

from werkzeug.security import check_password_hash


def userLoginHandler(UserModel, autorization):

    if request.method == 'POST':
        userLogin = request.form['login']
        userPassword = request.form['password']

        isUserLoginExist = UserModel.query.filter_by(login=userLogin).first()

        if isUserLoginExist != None:
            isPassworValid = check_password_hash(isUserLoginExist.password_hash, userPassword)

            if isPassworValid == True:
                autorization.loginUser(isUserLoginExist.id)

                return redirect('/')

        

    return render_template('user_login.html', isUserLogin=autorization.isUserLogin, isClientLogin=autorization.isClientLogin)