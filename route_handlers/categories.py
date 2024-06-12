import base64

from flask import render_template


# Определяем функцию categoriesHandler, которая принимает три параметра: CategoryModel, autorization и basket
def categoriesHandler(CategoryModel, autorization, basket):

    # Получаем все категории из базы данных
    CategoriesFromQuery = CategoryModel.query.all()

    # Инициализируем список категорий
    categories = []

    # Проходим по всем категориям из запроса
    for category in CategoriesFromQuery:

        # Кодируем изображение категории в формат base64 и декодируем его в строку ascii
        categoryImage = base64.b64encode(
            category.image).decode('ascii')

        # Добавляем категорию в список категорий
        categories.append({
            'id': category.id,
            'name': category.name,
            'discription': category.discription,
            'categoryImage': categoryImage
        })

    # Возвращаем результат рендеринга шаблона 'categories.html' с переданными параметрами
    return render_template('categories.html', categories=categories, autorization=autorization, basket=basket)
