class Student:
    def __init__(self, name, score):
        self.name = name
        if score < 0 or score > 10:
            print("Lỗi!")
        else:
            self.score = score

    def display(self):
        print("Sinh viên", self.name, "có điểm là", self.score)

s1 = Student("Thảo", 8)
s2 = Student("Vân", 10)

s1.display()
s2.display()