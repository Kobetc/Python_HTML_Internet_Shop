import base64

from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy


def categoriesHandler(CategoryModel, PositionModel, autorization):
    if request.method == 'POST':
        categoryId = request.form['id']

        return render_template('positions.html', categories=categories, autorization=autorization)

    CategoriesFromQuery = CategoryModel.query.all()

    categories = []

    for category in CategoriesFromQuery:

        categoryImage = base64.b64encode(
            category.image).decode('ascii')

        categories.append({
            'id': category.id,
            'name': category.name,
            'discription': category.discription,
            'categoryImage': categoryImage
        })

    return render_template('categories.html', categories=categories, autorization=autorization)
