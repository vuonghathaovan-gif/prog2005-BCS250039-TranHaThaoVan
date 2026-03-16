class SinhVien:
    so_luong = 0
    def __init__(self, ten, diem):
        self.ten = ten
        self.diem = diem
        SinhVien.so_luong += 1
    @classmethod
    def dem_sinh_vien(cls):
        return cls.so_luong
n = int(input("Nhập số sinh viên: "))
for i in range(n):
    print(f"Nhập thông tin SV {i + 1}:")
    ten = input("Tên: ")
    diem = float(input("Điểm: "))
    SinhVien(ten, diem)

print(f"Số SV đã tạo: {SinhVien.dem_sinh_vien()}")
