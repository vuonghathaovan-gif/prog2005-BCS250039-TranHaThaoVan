num = input("Nhập một số nguyên dương 5 chữ số: ")

if len(num) == 5 and num.isdigit():
    max_digit = max(int(d) for d in num)
    print(f"Chữ số lớn nhất trong {num} là {max_digit}.")
else:
    print("Số nhập không phải là số nguyên dương 5 chữ số.")
