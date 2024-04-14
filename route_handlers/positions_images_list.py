import base64

from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy


def positionsImagesListHandler(ImageModel, PositionModel, db: SQLAlchemy, autorization, basket):

    if request.method == 'POST':
        imageId = request.form['id']

        image = ImageModel.query.filter_by(id=imageId).first()

        if (image != None):
            db.session.delete(image)
            db.session.commit()

    imagesFromQuery = ImageModel.query.all()

    images = []

    for image in imagesFromQuery:
        positionName = "Позиция отсутствует"

        position = PositionModel.query.filter_by(id=image.position_id).first()

        if position != None:
            positionName = position.name

        images.append({
            'id': image.id,
            'position': positionName,
            'name': image.name,
            'data': base64.b64encode(image.data).decode('ascii')
        })

    return render_template('positions_images_list.html', images=images, autorization=autorization, basket=basket)
