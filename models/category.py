from flask_sqlalchemy import SQLAlchemy


def createCategoryModel(db: SQLAlchemy):

    class CategoryModel(db.Model):

        __tablename__ = 'categories'

        # Создаем столбец 'id' как первичный ключ
        id = db.Column(db.Integer(), primary_key=True)
        # Создаем столбец 'name', каждое имя должно быть уникальным и не может быть пустым
        name = db.Column(db.String(100), unique=True, nullable=False)
        # Создаем столбец 'discription', описание может повторяться и не может быть пустым
        discription = db.Column(db.Text, unique=False, nullable=False)
        # Создаем столбец 'image', изображение может повторяться и не может быть пустым
        image = db.Column(db.BLOB, unique=False, nullable=False)

        def __repr__(self):
            return "<{}:{}>".format(self.id, self.name)

    return CategoryModel
