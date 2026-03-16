class Product:
    def __init__(self, price):
        self.price = price
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            raise ValueError(">0")
    def __str__(self):
        return f"Giá sp: {self._price}"
try:
    user_input = input("Nhập giá sp: ")
    p = Product(float(user_input))
    print(p)
except ValueError as e:
    print(f"Lỗi: {e}")