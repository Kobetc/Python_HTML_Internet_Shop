from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy

from werkzeug.security import generate_password_hash, check_password_hash


def addNewCategoryHandler(CategoryModel, db: SQLAlchemy, autorization, basket):

    if request.method == 'POST':

        categoryName = request.form['name']
        categoryDiscription = request.form['discription']
        image = list(request.files.listvalues())[0]
        fileData = image[0].read()

        isCategoryNameExist = CategoryModel.query.filter_by(
            name=categoryName).first()

        if (isCategoryNameExist != None):
            return 'ОШИБКА !!! Категория с таким именем существует.'

        newCategory = CategoryModel(
            name=categoryName,
            discription=categoryDiscription,
            image=fileData
        )

        try:
            db.session.add(newCategory)
            db.session.commit()

            return render_template('add_new_category.html', autorization=autorization, basket=basket)
        except:
            return 'ОШИБКА !!! При сохранении категории в базу.'
    else:
        return render_template('add_new_category.html', autorization=autorization, basket=basket)
