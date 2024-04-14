import base64

from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy


def usersListHandler(UserModel, db: SQLAlchemy, autorization, basket):

    if request.method == 'POST':
        userId = request.form['id']

        user = UserModel.query.filter_by(id=userId).first()

        if (user != None):
            db.session.delete(user)
            db.session.commit()

    UsersFromQuery = UserModel.query.all()

    users = []

    for user in UsersFromQuery:

        users.append({
            'id': user.id,
            'name': user.name,
            'login': user.login
        })

    return render_template('users_list.html', users=users, autorization=autorization, basket=basket)
