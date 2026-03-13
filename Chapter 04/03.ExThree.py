def kiem_tra_key(dictionary, key):
    if key in dictionary:
        print(f"Key '{key}' tồn tại trong dic")
    else:
        print(f"Key '{key}' không tồn tại trong dic")
so_cap = int(input("Nhập số lượng cặp key-value: "))
thong_tin = {}
for i in range(so_cap):
    key = input(f"Nhập key thứ {i + 1}: ")
    value = input(f"Nhập value cho '{key}': ")
    thong_tin[key] = value
print(f"Dictionary: {thong_tin}")
key_can_tim = input("Nhập key cần kiểm tra: ")
kiem_tra_key(thong_tin, key_can_tim)