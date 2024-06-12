from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy


# Определяем функцию для обработки добавления новой категории
def addNewCategoryHandler(CategoryModel, db: SQLAlchemy, autorization, basket):

    # Проверяем, является ли метод запроса POST
    if request.method == 'POST':

        # Получаем имя категории из формы
        categoryName = request.form.get('name')
        # Получаем описание категории из формы
        categoryDiscription = request.form.get('discription')
        # Получаем изображение из формы
        image = list(request.files.listvalues())[0]
        # Читаем данные изображения
        fileData = image[0].read()

        # Проверяем, существует ли уже категория с таким именем
        isCategoryNameExist = CategoryModel.query.filter_by(
            name=categoryName).first()

        # Если категория с таким именем уже существует, возвращаем ошибку
        if (isCategoryNameExist != None):
            return 'ОШИБКА !!! Категория с таким именем существует.'

        # Создаем новую категорию
        newCategory = CategoryModel(
            name=categoryName,
            discription=categoryDiscription,
            image=fileData
        )

        # Пытаемся сохранить новую категорию в базе данных
        try:
            db.session.add(newCategory)
            db.session.commit()

            # Если сохранение прошло успешно, рендерим шаблон с формой добавления новой категории
            return render_template('add_new_category.html', autorization=autorization, basket=basket)
        except:
            # Если при сохранении произошла ошибка, возвращаем сообщение об ошибке
            return 'ОШИБКА !!! При сохранении категории в базу.'
    else:
        # Если метод запроса не POST, рендерим шаблон с формой добавления новой категории
        return render_template('add_new_category.html', autorization=autorization, basket=basket)
