def tinh_tong(n):
    if n == 1:
        return 1
    return n + tinh_tong(n - 1)
n = int(input("Nhap n: "))
print(tinh_tong(n))
