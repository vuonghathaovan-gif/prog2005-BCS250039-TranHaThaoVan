class Book:
    def __init__(self, name, price):
        self._name = name
        self._price = price
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, price):
        self._price = price
books = [
    Book("Book 1", 30000),
    Book("Book 2", 50000),
    Book("Book 3", 100000)
]
tong = 0
for b in books:
    tong += b.price
f = open("books.txt", "w")
for b in books:
    f.write(b.name + ";" + str(b.price) + "\n")
f.write("Tong;" + str(tong) + "\n")
f.close()