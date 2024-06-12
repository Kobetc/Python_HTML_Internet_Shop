import base64

from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy


# Определяем функцию для обработки списка категорий
def categoriesListHandler(CategoryModel, db: SQLAlchemy, autorization, basket):

    # Проверяем, является ли метод запроса POST
    if request.method == 'POST':
        # Получаем id категории из формы
        categoryId = request.form['id']

        # Ищем категорию по id в базе данных
        category = CategoryModel.query.filter_by(id=categoryId).first()

        # Если категория найдена, удаляем ее из базы данных
        if (category != None):
            db.session.delete(category)
            db.session.commit()

    # Получаем все категории из базы данных
    CategoriesFromQuery = CategoryModel.query.all()

    # Создаем пустой список для категорий
    categories = []

    # Проходимся по каждой категории из запроса
    for category in CategoriesFromQuery:

        # Кодируем изображение категории в base64
        categoryImage = base64.b64encode(
            category.image).decode('ascii')

        # Добавляем информацию о категории в список
        categories.append({
            'id': category.id,
            'name': category.name,
            'discription': category.discription,
            'categoryImage': categoryImage
        })

    # Рендерим шаблон с списком категорий
    return render_template('categories_list.html', categories=categories, autorization=autorization, basket=basket)
