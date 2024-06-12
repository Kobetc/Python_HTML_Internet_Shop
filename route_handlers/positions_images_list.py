import base64

from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy


# Определяем функцию обработчика списка изображений позиций
def positionsImagesListHandler(ImageModel, PositionModel, db: SQLAlchemy, autorization, basket):

    # Проверяем, является ли метод запроса POST
    if request.method == 'POST':

        # Получаем ID изображения из формы
        imageId = request.form.get('id')

        # Ищем изображение по ID
        image = ImageModel.query.filter_by(id=imageId).first()

        # Если изображение существует
        if (image != None):

            # Удаляем изображение из базы данных
            db.session.delete(image)

            # Применяем изменения в базе данных
            db.session.commit()

    # Получаем все изображения из базы данных
    imagesFromQuery = ImageModel.query.all()

    # Создаем пустой список для изображений
    images = []

    # Для каждого изображения в запросе
    for image in imagesFromQuery:

        # Устанавливаем имя позиции по умолчанию
        positionName = "Позиция отсутствует"

        # Ищем позицию по ID
        position = PositionModel.query.filter_by(id=image.position_id).first()

        # Если позиция существует
        if position != None:

            # Устанавливаем имя позиции
            positionName = position.name

        # Добавляем изображение в список изображений
        images.append({
            'id': image.id,
            'position': positionName,
            'name': image.name,
            'data': base64.b64encode(image.data).decode('ascii')
        })

    # Возвращаем шаблон с данными об изображениях, авторизации и корзине
    return render_template('positions_images_list.html', images=images, autorization=autorization, basket=basket)
