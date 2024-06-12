# Определяем класс Basket для работы с корзиной покупок
class Basket():

    # Инициализируем корзину при создании объекта класса
    def __init__(self):
        # Создаем словарь для хранения товаров в корзине
        self.basket = {}
        # Устанавливаем начальное количество товаров в корзине равное 0
        self.basketLen = 0
        # Устанавливаем начальную стоимость товаров в корзине равную 0
        self.basketPrice = 0

    # Определяем метод для очистки корзины
    def clearBasket(self):
        # Очищаем словарь с товарами
        self.basket.clear()
        # Устанавливаем количество товаров в корзине равное 0
        self.basketLen = 0
        # Устанавливаем стоимость товаров в корзине равную 0
        self.basketPrice = 0

    # Определяем метод для удаления определенного товара из корзины
    def clearBasketPosition(self, positionId):
        # Если товар с таким id есть в корзине, удаляем его
        if str(positionId) in self.basket:
            del self.basket[str(positionId)]
        # Пересчитываем количество товаров в корзине
        self.calcBasketLen()
        # Пересчитываем стоимость товаров в корзине
        self.calcBasketPrice()

    # Определяем метод для добавления товара в корзину
    def addPositionToBasket(self, position):
        # Если товар с таким id уже есть в корзине, увеличиваем его количество на 1
        if str(position.id) in self.basket:
            self.basket[str(position.id)] = {
                "position": position, "count": self.basket[str(position.id)]["count"] + 1}
        # Если товара с таким id еще нет в корзине, добавляем его
        else:
            self.basket[str(position.id)] = {
                "position": position, "count": 1}
        # Пересчитываем количество товаров в корзине
        self.calcBasketLen()
        # Пересчитываем стоимость товаров в корзине
        self.calcBasketPrice()

    # Определяем метод для увеличения количества определенного товара в корзине
    def plusPositionToBasket(self, positionId):
        # Если товар с таким id есть в корзине, увеличиваем его количество на 1
        if str(positionId) in self.basket:
            self.basket[str(positionId)] = {
                "position": self.basket[str(positionId)]["position"], "count": self.basket[str(positionId)]["count"] + 1}
        # Пересчитываем количество товаров в корзине
        self.calcBasketLen()
        # Пересчитываем стоимость товаров в корзине
        self.calcBasketPrice()

    # Определяем метод для уменьшения количества определенного товара в корзине
    def minusPositionToBasket(self, positionId):
        # Если товар с таким id есть в корзине и его количество больше 0, уменьшаем его количество на 1
        if str(positionId) in self.basket and self.basket[str(positionId)]["count"] > 0:
            self.basket[str(positionId)] = {
                "position": self.basket[str(positionId)]["position"], "count": self.basket[str(positionId)]["count"] - 1}
        # Пересчитываем количество товаров в корзине
        self.calcBasketLen()
        # Пересчитываем стоимость товаров в корзине
        self.calcBasketPrice()

    # Определяем метод для подсчета количества товаров в корзине
    def calcBasketLen(self):
        self.basketLen = len(self.basket)

    # Определяем метод для подсчета стоимости товаров в корзине
    def calcBasketPrice(self):
        # Задаем начальное значение стоимости равное 0
        price = 0
        # Проходимся по каждому товару в корзине
        for positionId in self.basket:
            # Получаем количество данного товара в корзине
            positionCount = self.basket[positionId]["count"]
            # Получаем стоимость данного товара
            positionPrice = self.basket[positionId]["position"].price

            # Увеличиваем общую стоимость на стоимость данного товара, умноженную на его количество
            price = price + int(positionCount) * float(positionPrice)

        # Устанавливаем общую стоимость товаров в корзине
        self.basketPrice = price
