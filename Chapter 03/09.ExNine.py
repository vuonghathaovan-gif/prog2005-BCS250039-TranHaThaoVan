input_str = input("Nhập danh sách số: ")
numbers = list(map(int, input_str.split()))

print("Các số lẻ trong danh sách:")
for num in numbers:
    if num % 2 != 0:
        print(num, end=" ")
print()
