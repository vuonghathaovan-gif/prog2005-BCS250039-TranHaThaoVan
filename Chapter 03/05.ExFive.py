def insertion_sort_giam_dan(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Sắp xếp giảm dần: dịch phần tử nhỏ hơn sang phải
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

input_str = input("Nhập danh sách số thực (cách nhau bởi dấu cách): ")
numbers = list(map(float, input_str.split()))
print("Danh sách sau khi sắp xếp giảm dần:", insertion_sort_giam_dan(numbers))
