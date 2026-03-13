while True:
    n = int(input("Nhập số từ 1-9 (Nhập 1 số ngoài khoảng để thoát vòng) : "))
    if 1 <= n <= 9:
        print(f"Bảng cửu chương {n}:")
        for i in range(1, 10):
            print(f"{n} x {i} = {n*i}")
    else:
        break
