from flask import render_template, request


def cartHandler(autorization, basket):

    print(basket)

    if request.method == 'POST':
        pass

    return render_template('cart.html', autorization=autorization, basket=basket)
