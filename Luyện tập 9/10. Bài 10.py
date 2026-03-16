class SinhVien:
    def __init__(self, ten, diem):
        self.ten = ten
        self.diem = diem

    def __eq__(self, other):
        if isinstance(other, SinhVien):
            return self.diem == other.diem
        return False

print("Sinh viên 1:")
ten1 = input("Tên: ")
diem1 = float(input("Điểm: "))
sv1 = SinhVien(ten1, diem1)

print("Sinh viên 2:")
ten2 = input("Tên: ")
diem2 = float(input("Điểm: "))
sv2 = SinhVien(ten2, diem2)

if sv1 == sv2:
    print(f"{sv1.ten} và {sv2.ten} bằng điểm")
elif sv1.diem > sv2.diem:
    print(f"{sv1.ten}  cao hơn {sv2.ten}")
else:
    print(f"{sv2.ten} cao hơn {sv1.ten} ")
