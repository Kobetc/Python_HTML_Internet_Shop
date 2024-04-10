import base64

from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy


def positionsListHandler(PositionModel, ImageModel, db: SQLAlchemy, autorization):

    if request.method == 'POST':
        positionId = request.form['id']

        position = PositionModel.query.filter_by(id=positionId).first()

        if (position != None):
            db.session.delete(position)
            db.session.commit()


    positionsFromQuery = PositionModel.query.all()

    positions = []

    for position in positionsFromQuery:
        imagesFromQuery = ImageModel.query.filter_by(position_id = position.id).all()

        positionImages = []
        for image in imagesFromQuery:
            if len(image.name):
                positionImages.append({
                    'name': image.name, 
                    'data': base64.b64encode(image.data).decode('ascii')
                })

        positions.append({
            'id': position.id, 
            'name': position.name, 
            'discription': position.discription,
            'price': position.price,
            'positionImages': positionImages
            })

    return render_template('positions_list.html', autorization = autorization)

