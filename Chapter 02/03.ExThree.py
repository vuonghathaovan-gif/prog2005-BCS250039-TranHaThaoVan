while True:
    try:
        n = int(input("Nhập vào số lượng số Fibonacci cần in: "))
        if n > 0:
            break
        else:
            print("Yêu cầu nhập số dương")
    except ValueError:
        print("Nhập số nguyên hợp lệ")
print(f"\n{n} số đầu tiên trong dãy Fibonacci:")

a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
