from flask_sqlalchemy import SQLAlchemy


def createClientModel(db: SQLAlchemy):

    class ClientModel(db.Model):
        
        __tablename__ = 'clients'

        id = db.Column(db.Integer(), primary_key=True)
        name = db.Column(db.String(100))
        login = db.Column(db.String(50), nullable=False, unique=True)
        email = db.Column(db.String(100), nullable=False, unique=True)
        password_hash = db.Column(db.String(100), nullable=False)

        def __repr__(self):
            return "<{}:{}>".format(self.id, self.name, self.email, self.login)
        
    return ClientModel
        