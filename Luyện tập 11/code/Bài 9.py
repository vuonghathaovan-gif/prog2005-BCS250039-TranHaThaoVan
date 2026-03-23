hang = int(input("Nhập số hàng: "))
cot = int(input("Nhập số cột : "))

def nhap_ma_tran(ten_ma_tran, hang, cot):
    print(f"Nhập ma trận {ten_ma_tran} ({hang}x{cot}):")
    ma_tran = []
    for i in range(hang):
        hang_ht = []
        for j in range(cot):
            while True:
                gia_tri = input(f"  {ten_ma_tran}[{i}][{j}] = ")
                if gia_tri.strip() == "":
                    print("Lỗi, nhập lại.")
                else:
                    try:
                        so = float(gia_tri)
                        hang_ht.append(so)
                        break
                    except ValueError:
                        print("ko hợp lệ, nhâp lại.")
        ma_tran.append(hang_ht)
    return ma_tran
def in_ma_tran(ma_tran):
    for hang in ma_tran:
        hang_str = ""
        for j in range(len(hang)):
            gia_tri = hang[j]
            if gia_tri == int(gia_tri):
                hang_str += f"{int(gia_tri):6}"
            else:
                hang_str += f"{gia_tri:6.1f}"
        print(hang_str)

A = nhap_ma_tran("A", hang, cot)
B = nhap_ma_tran("B", hang, cot)

C = []
for i in range(hang):
    hang_c = []
    for j in range(cot):
        hang_c.append(A[i][j] + B[i][j])
    C.append(hang_c)

print("Mt A:")
in_ma_tran(A)
print("Mt B:")
in_ma_tran(B)
print("Mt tổng")
in_ma_tran(C)