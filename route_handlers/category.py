import base64

from flask import render_template, request

from autorization import Autorization
from basket import Basket


def categoryHandler(id, PositionModel, ImageModel, CategoryModel, autorization: Autorization, basket: Basket):

    if request.method == 'POST':
        positionId = request.form['id']

        position = PositionModel.query.filter_by(id=positionId).first()

        print(position, basket)

        if position != None:
            basket.addPositionToBasket(position)

    positionsFromQuery = PositionModel.query.filter_by(
        category_id=id).all()

    positions = []

    for position in positionsFromQuery:
        imagesFromQuery = ImageModel.query.filter_by(
            position_id=position.id).all()

        positionImages = []
        for image in imagesFromQuery:
            if len(image.name):
                positionImages.append({
                    'name': image.name,
                    'data': base64.b64encode(image.data).decode('ascii')
                })

        positionCategoryName = "Категория отсутствует"

        categoryFromQuery = CategoryModel.query.filter_by(
            id=position.category_id).first()

        if categoryFromQuery != None:
            positionCategoryName = categoryFromQuery.name

        positions.append({
            'id': position.id,
            'name': position.name,
            'discription': position.discription,
            'price': position.price,
            'categoryName': positionCategoryName,
            'positionImages': positionImages
        })

    return render_template('category.html', positions=positions, autorization=autorization, basket=basket)
