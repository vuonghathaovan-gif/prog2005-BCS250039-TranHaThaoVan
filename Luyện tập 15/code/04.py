# Bài 4
a = float(input("Nhập điểm m1: "))
b = float(input("Nhập điểm m2: "))
c = float(input("Nhập điểm m3: "))
tb = (a + b + c) / 3
if tb >= 8:
    print("Giỏi")
elif tb >= 6.5:
    print("Khá")
elif tb >= 5.0:
    print("Trung bình")
else:
    print("Yếu")
