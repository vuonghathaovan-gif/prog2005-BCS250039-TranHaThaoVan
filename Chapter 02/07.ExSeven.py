while True:
    try:
        a = int(input("Nhập vào số nguyên dương thứ nhất: "))
        b = int(input("Nhập vào số nguyên dương thứ hai: "))
        if a > 0 and b > 0:
            break
        else:
            print("Nhập các số nguyên dương")
    except ValueError:
        print("Nhập số nguyên hợp lệ")

    # Thuật toán Euclid
so_a, so_b = a, b
while b != 0:
    a, b = b, a % b
print(f"USCLN của {so_a} và {so_b} là: {a}")
