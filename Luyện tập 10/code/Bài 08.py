strings = []
for i in range(5):
    s = input("Nhập chuỗi thứ {}: ".format(i + 1))
    strings.append(s)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if len(arr[j]) < len(arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        print("Sau bước {}: {}".format(i + 1, arr))
        if not swapped:
            break

bubble_sort(strings)
print("KQ cuối: ", strings)