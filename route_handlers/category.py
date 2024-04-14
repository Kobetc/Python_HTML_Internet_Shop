import base64

from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy


def categoryHandler(id: int, PositionModel, ImageModel, CategoryModel, db: SQLAlchemy, autorization):

    if request.method == 'POST':
        pass

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

    return render_template('category.html', positions=positions, autorization=autorization)
