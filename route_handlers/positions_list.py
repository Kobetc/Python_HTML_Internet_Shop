import base64

from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy


# Определяем функцию обработчика списка позиций
def positionsListHandler(PositionModel, ImageModel, CategoryModel, db: SQLAlchemy, autorization, basket):

    # Проверяем, является ли метод запроса POST
    if request.method == 'POST':

        # Получаем ID позиции из формы
        positionId = request.form.get('id')

        # Ищем позицию по ID
        position = PositionModel.query.filter_by(id=positionId).first()

        # Получаем все изображения для данной позиции
        positionImages = ImageModel.query.filter_by(
            position_id=positionId).all()

        # Если позиция существует
        if (position != None):

            # Удаляем позицию из базы данных
            db.session.delete(position)

        # Для каждого изображения в списке изображений
        for image in positionImages:

            # Удаляем изображение из базы данных
            db.session.delete(image)

        # Применяем изменения в базе данных
        db.session.commit()

    # Получаем все позиции из базы данных
    positionsFromQuery = PositionModel.query.all()

    # Создаем пустой список для позиций
    positions = []

    # Для каждой позиции в запросе
    for position in positionsFromQuery:

        # Получаем все изображения для данной позиции
        imagesFromQuery = ImageModel.query.filter_by(
            position_id=position.id).all()

        # Создаем пустой список для изображений позиции
        positionImages = []

        # Для каждого изображения в запросе
        for image in imagesFromQuery:

            # Если имя изображения не пустое
            if len(image.name):

                # Добавляем изображение в список изображений позиции
                positionImages.append({
                    'name': image.name,
                    'data': base64.b64encode(image.data).decode('ascii')
                })

        # Устанавливаем имя категории по умолчанию
        positionCategoryName = "Категория отсутствует"

        # Ищем категорию по ID
        categoryFromQuery = CategoryModel.query.filter_by(
            id=position.category_id).first()

        # Если категория существует
        if categoryFromQuery != None:

            # Устанавливаем имя категории
            positionCategoryName = categoryFromQuery.name

        # Добавляем позицию в список позиций
        positions.append({
            'id': position.id,
            'name': position.name,
            'discription': position.discription,
            'price': position.price,
            'categoryName': positionCategoryName,
            'positionImages': positionImages
        })

    # Возвращаем шаблон с данными о позициях, авторизации и корзине
    return render_template('positions_list.html', positions=positions, autorization=autorization, basket=basket)
