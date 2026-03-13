import random

M = int(input("Số hàng: "))
N = int(input("Số cột: "))

matrix = []
for i in range(M):
    row = []
    for j in range(N):
        row.append(random.randint(1, 99))
    matrix.append(row)

print("Ma trận:")
for row in matrix:
    print(row)

r = int(input("Số hàng muốn hiển thị  (1-" + str(M) + "): ")) - 1
print("Hàng", r + 1, ":", matrix[r])

c = int(input("Nhập cột muốn hiển thị  (1-" + str(N) + "): ")) - 1
col = []
for i in range(M):
    col.append(matrix[i][c])
print("Cột", c + 1, ":", col)

max_val = matrix[0][0]
for i in range(M):
    for j in range(N):
        if matrix[i][j] > max_val:
            max_val = matrix[i][j]
print("Giá trị lớn nhất:", max_val)