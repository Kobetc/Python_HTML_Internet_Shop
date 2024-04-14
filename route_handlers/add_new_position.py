from typing import Type
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy


def addNewPositionHandler(PositionModel, ImageModel, CategoryModel, db: SQLAlchemy, autorization):

    categoriesList = CategoryModel.query.all()

    if request.method == 'POST':
        images = list(request.files.listvalues())[0]

        positionName = request.form['name']
        positionDiscription = request.form['discription']
        positionPrice = request.form['price']
        positionCategoryId = request.form['category_id']

        isUserPositionExist = PositionModel.query.filter_by(
            name=positionName).first()
        if (isUserPositionExist != None):
            return 'ОШИБКА !!! Позиция с таким именем существует.'

        newPosition = PositionModel(
            name=positionName,
            discription=positionDiscription,
            price=positionPrice,
            category_id=positionCategoryId
        )

        try:
            db.session.add(newPosition)
            db.session.commit()
        except:
            return 'ОШИБКА !!! При сохранении позиции в базу.'

        newPosition = PositionModel.query.filter_by(name=positionName).first()
        if (newPosition == None):
            return 'ОШИБКА !!! Позиция с id не найдена.'

        for image in images:

            if len(image.filename) > 0:

                fileData = image.read()

                newImage = ImageModel(
                    name=image.filename,
                    data=fileData,
                    position_id=newPosition.id
                )

                try:
                    db.session.add(newImage)
                    db.session.commit()
                except:
                    return 'ОШИБКА !!! При сохранении изображения в базу.'

    return render_template('add_new_position.html', categoriesList=categoriesList, autorization=autorization)
