n11 = int(input("Nhập số lượng phần tử: "))
mang = []
print("Nhập các số:")
for i in range(n11):
    so = int(input(f"  Phần tử {i+1}: "))
    mang.append(so)

print(f"\nMảng: {mang}")
gia_tri_max = mang[0]
gia_tri_min = mang[0]

for so in mang:
    if so > gia_tri_max:
        gia_tri_max = so
    if so < gia_tri_min:
        gia_tri_min = so

print(f"Giá trị lớn nhất: {gia_tri_max}")
print(f"Giá trị nhỏ nhất: {gia_tri_min}")
