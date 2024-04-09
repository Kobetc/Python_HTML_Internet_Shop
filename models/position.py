from flask_sqlalchemy import SQLAlchemy


def createPositionModel(db: SQLAlchemy):
    class PositionModel(db.Model):

        __tablename__ = 'positions'

        id = db.Column(db.Integer(), primary_key=True)
        name = db.Column(db.String(100), unique=True)
        discription = db.Column(db.Text, nullable=True)
        price = db.Column(db.Integer(), nullable=False)

        def __repr__(self):
            return "<{}:{}>".format(self.id, self.name)
        
    return PositionModel
        