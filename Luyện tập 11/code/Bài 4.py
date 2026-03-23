ds = [15, 3, 7, 2, 8, 11, 4, 13, 6, 17]
print(f"Danh sách ban đầu: {ds}")
so_them = int(input("Nhập 1 số để thêm: "))
ds.append(so_them)
print(f"Sau thêm {so_them}: {ds}")
k = int(input("Nhập k cần đếm: "))
dem = 0
for phan_tu in ds:
    if phan_tu == k:
        dem += 1
print(f"{k} xuất hiện {dem} lần.")
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
tong_snt = 0
ds_snt = []
for phan_tu in ds:
    if la_so_nguyen_to(phan_tu):
        ds_snt.append(phan_tu)
        tong_snt += phan_tu
print(f"Số nguyên tố:: {ds_snt}")
print(f"Tổng số nguyên tố: {tong_snt}")
ds_sap_xep = ds[:]
n = len(ds_sap_xep)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if ds_sap_xep[j] > ds_sap_xep[j + 1]:
            ds_sap_xep[j], ds_sap_xep[j + 1] = ds_sap_xep[j + 1], ds_sap_xep[j]
print(f"Danh sách sau sx: {ds_sap_xep}")
ds.clear()
print(f"Sau khi xóa danh sách: {ds}")