ten = input("Nhập tên sinh viên: ")
tuoi = int(input("Nhập tuổi: "))
diem_tb = float(input("Nhập điểm trung bình: "))

sinh_vien = (ten, tuoi, diem_tb)
ten_sv, tuoi_sv, diem_sv = sinh_vien
print(f"Tên          : {ten_sv}")
print(f"Tuổi         : {tuoi_sv}")
print(f"Điểm TB      : {diem_sv}")
if diem_sv >= 8.5:
    xep_loai = "Giỏi"
elif diem_sv >= 7.0:
    xep_loai = "Khá"
elif diem_sv >= 5.0:
    xep_loai = "Trung bình"
else:
    xep_loai = "Yếu"
print(f"Học lực: {xep_loai}")