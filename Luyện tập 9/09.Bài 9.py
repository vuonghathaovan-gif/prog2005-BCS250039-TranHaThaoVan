class Animal:
    def __init__(self, name):
        self.name = name
    def sound(self):
        print("...")
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def sound(self):
        print("Gâu gâu")
d = Dog("Milo")
print(f"Tên: {d.name}")
d.sound()

