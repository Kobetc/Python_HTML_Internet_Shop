from flask_sqlalchemy import SQLAlchemy


def createCategoryModel(db: SQLAlchemy):

    class CategoryModel(db.Model):

        __tablename__ = 'categories'

        id = db.Column(db.Integer(), primary_key=True)
        name = db.Column(db.String(100), unique=True, nullable=False)
        discription = db.Column(db.Text, unique=False, nullable=False)
        image = db.Column(db.BLOB, unique=False, nullable=False)

        def __repr__(self):
            return "<{}:{}>".format(self.id, self.name)

    return CategoryModel
