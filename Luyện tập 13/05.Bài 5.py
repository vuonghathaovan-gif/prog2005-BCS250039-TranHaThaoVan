class Flower:
    def __init__(self):
        self.__color = ""
 
    def get_color(self):
        return self.__color
 
    def set_color(self, color):
        self.__color = color
f = Flower()
f.set_color("Do")
print("Mau hoa:", f.get_color())
