from flask_sqlalchemy import SQLAlchemy


def createBasketModel(db: SQLAlchemy):
    class BasketModel(db.Model):

        __tablename__ = 'baskets'

        id = db.Column(db.Integer(), primary_key=True)
        user_id = db.Column(db.Integer(), unique=True, nullable=False)

        def __repr__(self):
            return "<{}:{}>".format(self.id, self.name)
        
    return BasketModel
        