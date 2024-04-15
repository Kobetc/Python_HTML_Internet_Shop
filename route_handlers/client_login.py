from flask import redirect, render_template, request

from werkzeug.security import check_password_hash


def clientLoginHandler(ClientModel, autorization, basket):

    if request.method == 'POST':
        userLogin = request.form.get('login')
        userPassword = request.form.get('password')

        isClientLoginExist = ClientModel.query.filter_by(
            login=userLogin).first()

        if isClientLoginExist != None:
            isPassworValid = check_password_hash(
                isClientLoginExist.password_hash, userPassword)

            if isPassworValid == True:
                autorization.loginClient(isClientLoginExist.name)

                return redirect('/')

    return render_template('client_login.html', autorization=autorization, basket=basket)
