FILE_NAME = "products.txt"

def them_san_pham():
    code = input("Mã sản phẩm:: ")
    name = input("Tên sản phẩm: ")
    price = float(input("Giá: "))
    f = open(FILE_NAME, "a", encoding="utf-8")
    f.write(code + ";" + name + ";" + str(price) + "\n")
    f.close()
    print("Đã thêm sản phẩm")

def hien_thi_san_pham():
    f = open(FILE_NAME, "r", encoding="utf-8")
    for line in f:
        parts = line.strip().split(";")
        print("Mã:", parts[0], "| Tên:", parts[1], "| Giá:", parts[2])
    f.close()

def sap_xep_giam_dan():
    f = open(FILE_NAME, "r", encoding="utf-8")
    products = []
    for line in f:
        parts = line.strip().split(";")
        products.append([parts[0], parts[1], float(parts[2])])
    f.close()

    for i in range(len(products)):
        for j in range(i + 1, len(products)):
            if products[i][2] < products[j][2]:
                products[i], products[j] = products[j], products[i]

    for p in products:
        print("Mã:", p[0], "| Tên:", p[1], "| Giá:", p[2])

print("1. Thêm")
print("2. In")
print("3. Sắp xếp")
choice = input("Chọn chức năng (1/2/3): ")

if choice == "1":
    them_san_pham()
elif choice == "2":
    hien_thi_san_pham()
elif choice == "3":
    sap_xep_giam_dan()