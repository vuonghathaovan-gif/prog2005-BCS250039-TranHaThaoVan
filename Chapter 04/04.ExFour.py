class Hoa:
    def __init__(self, ten, mau):
        self.ten = ten
        self.mau = mau

    def __str__(self):
        return f"Hoa: {self.ten}, Màu: {self.mau}"
ten_hoa = input("Nhập tên hoa: ")
mau_hoa = input("Nhập màu hoa: ")
hoa1 = Hoa(ten_hoa, mau_hoa)
print(hoa1)