n = int(input("Nhập n: "))
if n > 1:
    so_nguyen_to = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            so_nguyen_to = False
            break
    if so_nguyen_to:
        print(f"{n} là số nguyên tố.")
    else:
        print(f"{n} không phải là số nguyên tố.")
else:
    print("n phải lớn hơn 1.")
