so_nv = int(input("Nhập số lượng nhân viên: "))
ds_nhan_vien = []
for i in range(so_nv):
    print(f"\nNhân viên thứ {i + 1}:")
    ten = input("  Tên: ")
    tuoi = input("  Tuổi: ")
    ma_id = input("  ID: ")
    ds_nhan_vien.append({"ten": ten, "tuoi": tuoi, "id": ma_id})

with open("nhan_vien.txt", "w", encoding="utf-8") as f:
    f.write("Danh sách nv\n")
    for nv in ds_nhan_vien:
        f.write(f"Tên  : {nv['ten']}\n")
        f.write(f"Tuổi : {nv['tuoi']}\n")
        f.write(f"ID   : {nv['id']}\n")

with open("nhan_vien.csv", "w", encoding="utf-8") as f:
    f.write("Ten,Tuoi,ID\n")
    for nv in ds_nhan_vien:
        f.write(f"{nv['ten']},{nv['tuoi']},{nv['id']}\n")

with open("nhan_vien.txt", "r", encoding="utf-8") as f:
    print(f.read())
with open("nhan_vien.csv", "r", encoding="utf-8") as f:
    print(f.read())