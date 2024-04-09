import base64

from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy


def images_handler(ImageModel, db: SQLAlchemy):

    if request.method == 'POST':
        imageId = request.form['id']

        image = ImageModel.query.filter_by(id=imageId).first()

        if (image != None):
            db.session.delete(image)
            db.session.commit()

        imagesFromQuery = ImageModel.query.filter_by(position_id=1).all()
        images = [ {'id': image.id, 'position': image.position_id, 'name': image.name, 'data': base64.b64encode(image.data).decode('ascii')} for image in imagesFromQuery ]

        return render_template('images.html', images=images)


    imagesFromQuery = ImageModel.query.filter_by(position_id=1).all()
    images = [ {'id': image.id, 'position': image.position_id, 'name': image.name, 'data': base64.b64encode(image.data).decode('ascii')} for image in imagesFromQuery ]

    return render_template('images.html', images=images)

 