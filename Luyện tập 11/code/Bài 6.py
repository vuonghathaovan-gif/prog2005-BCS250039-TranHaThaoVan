so_nguoi = int(input("Nhập số lượng người cần nhập: "))
thong_tin = {}
for i in range(so_nguoi):
    print(f"\nNgười thứ {i + 1}:")
    ten = input("  Nhập tên: ")
    tuoi = int(input("  Nhập tuổi: "))
    thong_tin[ten] = tuoi
tong_tuoi = 0
for tuoi in thong_tin.values():
    tong_tuoi += tuoi
trung_binh = tong_tuoi / len(thong_tin)
print(f"Tuổi trung bình: {trung_binh:.2f}")