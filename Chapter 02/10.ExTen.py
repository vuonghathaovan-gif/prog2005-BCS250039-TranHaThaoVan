def tong_de_quy(n):
    if n == 1:
        return 1
    else:
        return n + tong_de_quy(n - 1)


while True:
    try:
        n = int(input("Nhập vào số nguyên dương n: "))
        if n > 0:
            break
        else:
            print("Nhập số dương")
    except ValueError:
        print("Nhập một số nguyên hợp lệ")

ket_qua = tong_de_quy(n)
print(f"Tổng các số từ 1 đến {n} là: {ket_qua}")
