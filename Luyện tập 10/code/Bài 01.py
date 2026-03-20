def lay_ten_file(duong_dan):
    vi_tri = -1
    for i in range(len(duong_dan) - 1, -1, -1):
        if duong_dan[i] == '\\' or duong_dan[i] == '/':
            vi_tri = i
            break
    return duong_dan[vi_tri + 1:]
def lay_ten_bai_hat(duong_dan):
    ten_file = lay_ten_file(duong_dan)
    vi_tri_cham = -1
    for i in range(len(ten_file) - 1, -1, -1):
        if ten_file[i] == '.':
            vi_tri_cham = i
            break
    if vi_tri_cham == -1:
        return ten_file
    return ten_file[:vi_tri_cham]
while True:
    duong_dan = input("Nhập đường dẫn (exit để thoát): ")
    if duong_dan == "exit":
        break
    print("Ten file:", lay_ten_file(duong_dan))
    print("Ten bai hat:", lay_ten_bai_hat(duong_dan))
