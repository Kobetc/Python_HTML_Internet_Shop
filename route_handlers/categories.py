import base64

from flask import render_template


def categoriesHandler(CategoryModel, autorization, basket):

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

    return render_template('categories.html', categories=categories, autorization=autorization, basket=basket)
