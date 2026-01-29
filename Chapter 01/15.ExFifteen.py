# Sinh viên 1
ten1 = input("Nhập tên sinh viên 1: ")
toan1 = float(input("Nhập điểm Toán: "))
ly1 = float(input("Nhập điểm Lý: "))
hoa1 = float(input("Nhập điểm Hóa: "))
dtb1 = (toan1 + ly1 + hoa1) / 3

# Sinh viên 2
ten2 = input("Nhập tên sinh viên 2: ")
toan2 = float(input("Nhập điểm Toán: "))
ly2 = float(input("Nhập điểm Lý: "))
hoa2 = float(input("Nhập điểm Hóa: "))
dtb2 = (toan2 + ly2 + hoa2) / 3

# Sinh viên 3
ten3 = input("Nhập tên sinh viên 3: ")
toan3 = float(input("Nhập điểm Toán: "))
ly3 = float(input("Nhập điểm Lý: "))
hoa3 = float(input("Nhập điểm Hóa: "))
dtb3 = (toan3 + ly3 + hoa3) / 3


print("Sinh viên:", ten1, "- Điểm trung bình:", round(dtb1, 2))
print("Sinh viên:", ten2, "- Điểm trung bình:", round(dtb2, 2))
print("Sinh viên:", ten3, "- Điểm trung bình:", round(dtb3, 2))