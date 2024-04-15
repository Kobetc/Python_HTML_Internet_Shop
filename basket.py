class Basket():

    def __init__(self):
        self.basket = {}
        self.basketLen = 0
        self.basketPrice = 0

    def clearBasket(self):
        self.basket.clear()
        self.basketLen = 0
        self.basketPrice = 0

    def clearBasketPosition(self, positionId):
        if str(positionId) in self.basket:
            del self.basket[str(positionId)]

        self.calcBasketLen()
        self.calcBasketPrice()

    def addPositionToBasket(self, position):

        if str(position.id) in self.basket:
            self.basket[str(position.id)] = {
                "position": position, "count": self.basket[str(position.id)]["count"] + 1}
        else:
            self.basket[str(position.id)] = {
                "position": position, "count": 1}

        self.calcBasketLen()
        self.calcBasketPrice()

    def plusPositionToBasket(self, positionId):

        if str(positionId) in self.basket:

            self.basket[str(positionId)] = {
                "position": self.basket[str(positionId)]["position"], "count": self.basket[str(positionId)]["count"] + 1}

        self.calcBasketLen()
        self.calcBasketPrice()

    def minusPositionToBasket(self, positionId):

        if str(positionId) in self.basket and self.basket[str(positionId)]["count"] > 0:

            self.basket[str(positionId)] = {
                "position": self.basket[str(positionId)]["position"], "count": self.basket[str(positionId)]["count"] - 1}

        self.calcBasketLen()
        self.calcBasketPrice()

    def calcBasketLen(self):
        self.basketLen = len(self.basket)

    def calcBasketPrice(self):
        price = 0

        for positionId in self.basket:
            positionCount = self.basket[positionId]["count"]
            positionPrice = self.basket[positionId]["position"].price

            price = price + int(positionCount) * float(positionPrice)

        self.basketPrice = price
