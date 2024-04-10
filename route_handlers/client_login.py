from flask import redirect, render_template, request

from werkzeug.security import check_password_hash


def clientLoginHandler(ClientModel, autorization):

    if request.method == 'POST':
        userLogin = request.form['login']
        userPassword = request.form['password']

        isClientLoginExist = ClientModel.query.filter_by(login=userLogin).first()

        if isClientLoginExist != None:
            isPassworValid = check_password_hash(isClientLoginExist.password_hash, userPassword)

            if isPassworValid == True:
                autorization.loginClient(isClientLoginExist.name)

                return redirect('/')

        

    return render_template('client_login.html', autorization = autorization)