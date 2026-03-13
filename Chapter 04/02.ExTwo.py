def tinh_diem_trung_binh(sinh_vien):
    tong_diem = sum(sinh_vien.values())
    trung_binh = tong_diem / len(sinh_vien)
    return trung_binh
so_sv = int(input("Nhập số lượng sinh viên: "))
sinh_vien = {}
for i in range(so_sv):
    ten = input(f"Nhập tên sinh viên thứ {i + 1}: ")
    diem = float(input(f"Nhập điểm của {ten}: "))
    sinh_vien[ten] = diem
print(f"Danh sách sinh viên: {sinh_vien}")
print(f"Điểm trung bình: {tinh_diem_trung_binh(sinh_vien):.2f}")