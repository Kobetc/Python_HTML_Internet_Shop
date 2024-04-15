from flask import render_template, request

from basket import Basket


def cartHandler(autorization, basket: Basket):

    if request.method == 'POST':
        positionId = request.form.get('id')
        plusPositionId = request.form.get('plus')
        minusPositionId = request.form.get('minus')

        if plusPositionId:
            basket.plusPositionToBasket(plusPositionId)
        elif minusPositionId:
            basket.minusPositionToBasket(minusPositionId)
        elif positionId == "-1":
            basket.clearBasket()
        else:
            basket.clearBasketPosition(positionId)

    return render_template('cart.html', autorization=autorization, basket=basket)
