class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

s1 = Student("Thảo", 8)
s2 = Student("Vân", 10)

print(s1.name, s1.score)
print(s2.name, s2.score)