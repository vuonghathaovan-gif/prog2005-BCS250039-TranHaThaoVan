def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print("Selection Sort:", arr)

n = int(input("Nhập số phần tử của mảng: "))
arr = []

for i in range(n):
    phan_tu = int(input(f"Nhập phần tử thứ {i+1}: "))
    arr.append(phan_tu)
selection_sort(arr)
print("Kết quả cuối cùng là: ",arr)