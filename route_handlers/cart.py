from flask import render_template, request, redirect

from basket import Basket


def cartHandler(autorization, basket: Basket):

    # Проверяем, является ли метод запроса POST
    if request.method == 'POST':
        # Получаем идентификатор позиции из формы
        positionId = request.form.get('id')
        # Получаем идентификатор позиции для увеличения количества из формы
        plusPositionId = request.form.get('plus')
        # Получаем идентификатор позиции для уменьшения количества из формы
        minusPositionId = request.form.get('minus')
        # Получаем команду на очистку корзины из формы
        clean = request.form.get('clean')
        # Получаем команду на оплату из формы
        pay = request.form.get('pay')

        # Выводим на печать команду на очистку и идентификатор позиции
        print(clean, positionId)

        # Если получена команда на увеличение количества позиции, увеличиваем количество
        if plusPositionId:
            basket.plusPositionToBasket(plusPositionId)
        # Если получена команда на уменьшение количества позиции, уменьшаем количество
        elif minusPositionId:
            basket.minusPositionToBasket(minusPositionId)
        # Если получен идентификатор позиции, очищаем эту позицию в корзине
        elif positionId != None:
            basket.clearBasketPosition(positionId)
        # Если получена команда на очистку корзины, очищаем корзину
        elif clean != None:
            basket.clearBasket()
        # Если получена команда на оплату, очищаем корзину и перенаправляем пользователя на главную страницу
        elif pay != None:
            basket.clearBasket()
            return redirect('/')

    # Возвращаем HTML-шаблон с данными о корзине и авторизации
    return render_template('cart.html', autorization=autorization, basket=basket)
