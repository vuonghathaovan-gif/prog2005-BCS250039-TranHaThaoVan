# Bài 8
class Product:
    def __init__(self, price):
        self.price = price
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("lỗi")
        self._price = value
p = Product(100)
print(p.price)
