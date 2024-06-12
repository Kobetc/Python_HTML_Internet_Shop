from typing import Type
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy


def addNewPositionHandler(PositionModel, ImageModel, CategoryModel, db: SQLAlchemy, autorization, basket):

    # Получаем список всех категорий из базы данных
    categoriesList = CategoryModel.query.all()

    # Проверяем, является ли метод запроса POST
    if request.method == 'POST':
        # Получаем изображения из формы
        images = list(request.files.listvalues())[0]

        # Получаем имя позиции из формы
        positionName = request.form.get('name')
        # Получаем описание позиции из формы
        positionDiscription = request.form.get('discription')
        # Получаем цену позиции из формы
        positionPrice = request.form.get('price')
        # Получаем идентификатор категории позиции из формы
        positionCategoryId = request.form.get('category_id')

        # Проверяем, существует ли уже позиция с таким именем
        isUserPositionExist = PositionModel.query.filter_by(
            name=positionName).first()
        # Если позиция с таким именем уже существует, возвращаем сообщение об ошибке
        if (isUserPositionExist != None):
            return 'ОШИБКА !!! Позиция с таким именем существует.'

        # Создаем новую позицию
        newPosition = PositionModel(
            name=positionName,
            discription=positionDiscription,
            price=positionPrice,
            category_id=positionCategoryId
        )

        # Пытаемся добавить новую позицию в базу данных
        try:
            db.session.add(newPosition)
            db.session.commit()
        # Если при сохранении позиции в базу данных произошла ошибка, возвращаем сообщение об ошибке
        except:
            return 'ОШИБКА !!! При сохранении позиции в базу.'

        # Ищем новую позицию в базе данных по имени
        newPosition = PositionModel.query.filter_by(name=positionName).first()
        # Если позиция не найдена, возвращаем сообщение об ошибке
        if (newPosition == None):
            return 'ОШИБКА !!! Позиция с id не найдена.'

        # Проходим по всем изображениям
        for image in images:

            # Если имя файла изображения не пустое
            if len(image.filename) > 0:

                # Читаем данные изображения
                fileData = image.read()

                # Создаем новое изображение
                newImage = ImageModel(
                    name=image.filename,
                    data=fileData,
                    position_id=newPosition.id
                )

                # Пытаемся добавить новое изображение в базу данных
                try:
                    db.session.add(newImage)
                    db.session.commit()
                # Если при сохранении изображения в базу данных произошла ошибка, возвращаем сообщение об ошибке
                except:
                    return 'ОШИБКА !!! При сохранении изображения в базу.'

    # Если метод запроса не POST, возвращаем HTML-шаблон для добавления новой позиции
    return render_template('add_new_position.html', categoriesList=categoriesList, autorization=autorization, basket=basket)
