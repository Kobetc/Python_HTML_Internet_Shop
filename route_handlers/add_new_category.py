from flask import redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

from werkzeug.security import generate_password_hash, check_password_hash


def addNewCategoryHandler(CategoryModel, db: SQLAlchemy, autorization):

    if request.method == 'POST':
        categoryName = request.form['name']
        categoryDiscription = request.form['discription']

        isCategoryNameExist = CategoryModel.query.filter_by(
            name=categoryName).first()

        if (isCategoryNameExist != None):
            return 'ОШИБКА !!! Категория с таким именем существует.'

        newCategory = CategoryModel(
            name=categoryName,
            discription=categoryDiscription,
        )

        try:
            db.session.add(newCategory)
            db.session.commit()

            return redirect('/')
        except:
            return 'ОШИБКА !!! При сохранении категории в базу.'
    else:
        return render_template('add_new_category.html', autorization=autorization)
