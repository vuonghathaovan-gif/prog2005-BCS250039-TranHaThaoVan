# Nhập số
so = float(input("Nhập một số: "))

# Kiểm tra số âm
if so < 0:
    print("Lỗi")
else:
    can = so ** 0.5
    print("Căn bậc hai của", so, "là:", can)