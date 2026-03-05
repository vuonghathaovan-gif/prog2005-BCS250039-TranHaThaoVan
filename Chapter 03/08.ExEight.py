input_str = input("Nhập danh sách số: ")
numbers = list(map(int, input_str.split()))

found = False
for num in numbers:
    if num > 10:
        print(f"Số đầu tiên lớn hơn 10 là: {num}")
        found = True
        break
if not found:
    print("Không có số nào lớn hơn 10 trong danh sách.")
