while True:
    try:
        n = int(input("Nhập vào một số dương: "))
        if n > 0:
            break
        else:
            print("Vui lòng nhập số dương!")
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ!")

if n < 2:
    print(f"{n} không phải là số nguyên tố")
else:
    la_nguyen_to = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            la_nguyen_to = False
            break

    if la_nguyen_to:
        print(f"{n} là số nguyên tố")
    else:
        print(f"{n} không phải là số nguyên tố")
