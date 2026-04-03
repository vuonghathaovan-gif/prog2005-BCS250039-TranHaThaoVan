mang = list(map(int, input("Nhap cac phan tu: ").split()))
so_le = []
sl=0
for x in mang:
    if x % 2 != 0:
        so_le.append(x)
        sl=sl+1
print(f"Các số lẻ:{so_le},Số lượng:{sl}")
snt = []
for x in mang:
    if x < 2:
        continue
    ok = True
    for i in range(2, x):
        if x % i == 0:
            ok = False
            break
    if ok:
        snt.append(x)
print("Số nguyên tố:",snt)