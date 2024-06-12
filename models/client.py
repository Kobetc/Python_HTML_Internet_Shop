from flask_sqlalchemy import SQLAlchemy


def createClientModel(db: SQLAlchemy):

    class ClientModel(db.Model):

        __tablename__ = 'clients'

        # Определение столбца id как первичного ключа
        id = db.Column(db.Integer(), primary_key=True)
        # Определение столбца name, который должен быть уникальным и не может быть пустым
        name = db.Column(db.String(100), unique=True, nullable=False)
        # Определение столбца login, который должен быть уникальным и не может быть пустым
        login = db.Column(db.String(50), unique=True, nullable=False)
        # Определение столбца email, который должен быть уникальным и не может быть пустым
        email = db.Column(db.String(100), unique=True, nullable=False)
        # Определение столбца password_hash, который не может быть пустым
        password_hash = db.Column(db.String(100), unique=False, nullable=False)

        def __repr__(self):
            return "<{}:{}>".format(self.id, self.name, self.email, self.login)

    return ClientModel
