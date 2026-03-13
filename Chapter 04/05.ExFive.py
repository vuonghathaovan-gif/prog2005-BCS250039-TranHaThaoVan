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
            print("Giá phải lớn hơn 0")
            self._price = 0
    def __str__(self):
        return f"Giá sản phẩm: {self._price}"
gia = float(input("Nhập giá sản phẩm: "))
p = Product(gia)
print(p)