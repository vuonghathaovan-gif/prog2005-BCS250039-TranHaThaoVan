class Student:
    def __init__(self, name, score):
        self.name = name
        if score < 0 or score > 10:
            print("Lỗi")
        else:
            self.score = score

s1 = Student("Thảo", 8)
s2 = Student("Vân", 15)