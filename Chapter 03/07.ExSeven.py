def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1
input_str = input("Nhập danh sách số: ")
numbers = list(map(int, input_str.split()))
target = int(input("Nhập số cần tìm: "))
index = linear_search(numbers, target)
if index != -1:
    print(f"Số {target} tìm thấy tại chỉ số: {index}")
else:
    print(f"Số {target} không tìm thấy trong danh sách.")
