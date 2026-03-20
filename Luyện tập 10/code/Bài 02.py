def motchuoi():
    chuoi = input("Nhập chuỗi: ")
    kytu = input("Nhập vào một ký tự: ")
    if len(kytu) != 1:
        print("Nhập 1 chữ.")
        return
    count = chuoi.count(kytu)
    print((count))
motchuoi()