from flask import render_template, request, redirect

from basket import Basket


def cartHandler(autorization, basket: Basket):

    if request.method == 'POST':
        positionId = request.form.get('id')
        plusPositionId = request.form.get('plus')
        minusPositionId = request.form.get('minus')
        clean = request.form.get('clean')
        pay = request.form.get('pay')

        print(clean, positionId)

        if plusPositionId:
            basket.plusPositionToBasket(plusPositionId)
        elif minusPositionId:
            basket.minusPositionToBasket(minusPositionId)
        elif positionId != None:
            basket.clearBasketPosition(positionId)
        elif clean != None:
            basket.clearBasket()
        elif pay != None:
            basket.clearBasket()
            return redirect('/')

    return render_template('cart.html', autorization=autorization, basket=basket)
