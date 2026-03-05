chuoi = input("Nhập chuỗi cần đảo ngược: ")
print(f'\nChuỗi gốc: "{chuoi}"')
# Cách 1:
dao_nguoc_slicing = chuoi[::-1]
print(f'Cách 1 (Slicing [::-1]):  "{dao_nguoc_slicing}"')
# Cách 2:
dao_nguoc_loop = ""
for ky_tu in chuoi:
    dao_nguoc_loop = ky_tu + dao_nguoc_loop
print(f'Cách 2 (Vòng lặp): "{dao_nguoc_loop}"')
