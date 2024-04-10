from flask_sqlalchemy import SQLAlchemy


def createImageModel(db: SQLAlchemy):
    class ImageModel(db.Model):
        
        __tablename__ = 'images'

        id = db.Column(db.Integer(), primary_key=True)
        name = db.Column(db.String(100), unique=False, nullable=False)
        data = db.Column(db.BLOB, unique=False, nullable=False)
        position_id = db.Column(db.Integer(), unique=False, nullable=False)

        def __repr__(self):
            return "<{}:{}>".format(self.id, self.name)

    return ImageModel
        