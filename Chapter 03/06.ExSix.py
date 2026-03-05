def bubble_sort(arr):
    n = len(arr)
    dem_hoan_doi = 0
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                dem_hoan_doi += 1
    return arr, dem_hoan_doi
# Nhập dữ liệu
input_str = input("Nhập danh sách số nguyên (cách nhau bởi dấu cách): ")
numbers = list(map(int, input_str.split()))

sorted_list, swaps = bubble_sort(numbers)
print("Danh sách đã sắp xếp:", sorted_list)
print(f"Số lần hoán đổi: {swaps}")
