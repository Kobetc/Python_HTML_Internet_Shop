from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy


# Определяем функцию обработчика списка пользователей
def usersListHandler(UserModel, db: SQLAlchemy, autorization, basket):

    # Проверяем, является ли метод запроса POST
    if request.method == 'POST':

        # Получаем ID пользователя из формы
        userId = request.form.get('id')

        # Ищем пользователя по ID
        user = UserModel.query.filter_by(id=userId).first()

        # Если пользователь найден
        if (user != None):

            # Удаляем пользователя из базы данных
            db.session.delete(user)

            # Применяем изменения в базе данных
            db.session.commit()

    # Получаем всех пользователей из базы данных
    UsersFromQuery = UserModel.query.all()

    # Создаем пустой список для пользователей
    users = []

    # Для каждого пользователя в запросе
    for user in UsersFromQuery:

        # Добавляем пользователя в список
        users.append({
            'id': user.id,
            'name': user.name,
            'login': user.login
        })

    # Возвращаем шаблон с данными о пользователях, авторизации и корзине
    return render_template('users_list.html', users=users, autorization=autorization, basket=basket)
