input_str = input("Nhập danh sách số: ")
numbers = list(map(int, input_str.split()))
sum_even = 0
print("Các số chẵn:")
for num in numbers:
    if num % 2 == 0:
        print(num, end=" ")
        sum_even += num
print(f"\nTổng các số chẵn: {sum_even}")
