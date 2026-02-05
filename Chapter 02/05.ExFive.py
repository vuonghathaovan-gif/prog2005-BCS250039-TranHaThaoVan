chuoi = input("Nhập vào một chuỗi: ")
ky_tu = input("Nhập vào ký tự cần đếm: ")
dem = 0
for i in chuoi:
    if i == ky_tu:
        dem += 1
print(f"Ký tự '{ky_tu}' xuất hiện {dem} lần trong chuỗi")
