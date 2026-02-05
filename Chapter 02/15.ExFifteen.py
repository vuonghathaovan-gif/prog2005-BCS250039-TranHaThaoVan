n = int(input("Nhập vào một số nguyên dương: "))
so_ban_dau = n
tong = 0
while n > 0:
    tong += n % 10
    n //= 10
print(f"Tổng các chữ số của {so_ban_dau} là: {tong}")
