import base64

from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy


def categoriesListHandler(CategoryModel, db: SQLAlchemy, autorization):

    if request.method == 'POST':
        categoryId = request.form['id']

        category = CategoryModel.query.filter_by(id=categoryId).first()

        if (category != None):
            db.session.delete(category)
            db.session.commit()

    CategoriesFromQuery = CategoryModel.query.all()

    categories = []

    for category in CategoriesFromQuery:

        categories.append({
            'id': category.id,
            'name': category.name,
            'discription': category.discription
        })

    return render_template('categories_list.html', categories=categories, autorization=autorization)
