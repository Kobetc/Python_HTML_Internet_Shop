from flask_sqlalchemy import SQLAlchemy


def createImageModel(db: SQLAlchemy):
    class ImageModel(db.Model):

        __tablename__ = 'images'

        # Определение столбца id как первичного ключа
        id = db.Column(db.Integer(), primary_key=True)
        # Определение столбца name, который не может быть пустым
        name = db.Column(db.String(100), unique=False, nullable=False)
        # Определение столбца data, который содержит данные изображения и не может быть пустым
        data = db.Column(db.BLOB, unique=False, nullable=False)
        # Определение столбца position_id, который не может быть пустым
        position_id = db.Column(db.Integer(), unique=False, nullable=False)

        def __repr__(self):
            return "<{}:{}>".format(self.id, self.name)

    return ImageModel
