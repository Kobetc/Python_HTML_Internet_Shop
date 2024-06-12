from flask_sqlalchemy import SQLAlchemy


def createPositionModel(db: SQLAlchemy):
    class PositionModel(db.Model):

        __tablename__ = 'positions'

        # Определение столбца id как первичного ключа
        id = db.Column(db.Integer(), primary_key=True)
        # Определение столбца name, который должен быть уникальным и не может быть пустым
        name = db.Column(db.String(100), unique=True, nullable=False)
        # Определение столбца discription, который содержит описание позиции и не может быть пустым
        discription = db.Column(db.Text, unique=False, nullable=False)
        # Определение столбца price, который содержит цену позиции и не может быть пустым
        price = db.Column(db.Integer(), unique=False, nullable=False)
        # Определение столбца category_id, который не может быть пустым
        category_id = db.Column(db.Integer(), unique=False, nullable=False)

        def __repr__(self):
            return "<{}:{}>".format(self.id, self.name)

    return PositionModel
