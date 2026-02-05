def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * giai_thua(n - 1)

while True:
    try:
        n = int(input("Nhập vào một số: "))
        if n >= 0:
            break
        else:
            print("Nhập số không âm")
    except ValueError:
        print("Nhập một số nguyên hợp lệ")

ket_qua = giai_thua(n)
print(f"{n}! = {ket_qua}")
