n = int(input("Nhập n: "))
tong = 0
for i in range(1, n + 1, 2):
    tong += i
print(f"Tổng số lẻ từ 1 đến {n} là {tong}.")
