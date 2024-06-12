import base64

from flask import render_template, request

from autorization import Autorization
from basket import Basket


def categoryHandler(id, PositionModel, ImageModel, CategoryModel, autorization: Autorization, basket: Basket):

    # Проверяем, является ли метод запроса POST
    if request.method == 'POST':
        # Получаем значение 'id' из формы
        positionId = request.form['id']

        # Проверяем, существует ли позиция с таким id в базе данных
        position = PositionModel.query.filter_by(id=positionId).first()

        # Если позиция с таким id существует
        if position != None:
            # Добавляем позицию в корзину
            basket.addPositionToBasket(position)

    # Получаем все позиции с указанным id категории
    positionsFromQuery = PositionModel.query.filter_by(
        category_id=id).all()

    # Инициализируем список позиций
    positions = []

    # Проходим по всем позициям из запроса
    for position in positionsFromQuery:
        # Получаем все изображения для текущей позиции
        imagesFromQuery = ImageModel.query.filter_by(
            position_id=position.id).all()

        # Инициализируем список изображений для текущей позиции
        positionImages = []
        # Проходим по всем изображениям из запроса
        for image in imagesFromQuery:
            # Если имя изображения не пустое
            if len(image.name):
                # Добавляем изображение в список изображений для текущей позиции
                positionImages.append({
                    'name': image.name,
                    'data': base64.b64encode(image.data).decode('ascii')
                })

        # Устанавливаем значение по умолчанию для имени категории позиции
        positionCategoryName = "Категория отсутствует"

        # Проверяем, существует ли категория с указанным id в базе данных
        categoryFromQuery = CategoryModel.query.filter_by(
            id=position.category_id).first()

        # Если категория с таким id существует
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

    # Возвращаем результат рендеринга шаблона 'category.html' с переданными параметрами
    return render_template('category.html', positions=positions, autorization=autorization, basket=basket)
