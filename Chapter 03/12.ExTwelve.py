def input_matrix(rows, cols):
    print(f"Nhập ma trận {rows}x{cols}:")
    mat = []
    for i in range(rows):
        row = list(map(int, input(f"Nhập hàng {i+1} (cách nhau bởi dấu cách): ").split()))
        mat.append(row)
    return mat

def add_matrices(A, B):
    rows = len(A)
    cols = len(A[0])
    C = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            C[i][j] = A[i][j] + B[i][j]
    return C

m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))

A = input_matrix(m, n)
B = input_matrix(m, n)

C = add_matrices(A, B)
print("Ma trận tổng C = A + B:")
for row in C:
    print(row)
