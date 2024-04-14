class Basket():

    def __init__(self):
        self.basket = {}
        self.basketLen = 0
        self.basketPrice = 0

    def clearBasket(self):
        self.basket.clear()

    def addPositionToBasket(self, position):

        if str(position.id) in self.basket:
            self.basket[str(position.id)] = {
                "position": position, "count": self.basket[str(position.id)]["count"] + 1}
        else:
            self.basket[str(position.id)] = {
                "position": position, "count": 1}

        self.basketLen = len(self.basket)

        price = 0

        for positionId in self.basket:
            positionCount = self.basket[positionId]["count"]
            positionPrice = self.basket[positionId]["position"].price

            price = price + int(positionCount) * float(positionPrice)

        self.basketPrice = price

        print(self.basket, self.basketLen, self.basketPrice)
