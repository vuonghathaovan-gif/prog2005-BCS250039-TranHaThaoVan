def tim_max_min():
    a = int(input("Nhập số thứ nhất (a): "))
    b = int(input("Nhập số thứ hai (b): "))
    c = int(input("Nhập số thứ ba (c): "))

    so_lon = a
    if b > so_lon:
        so_lon = b
    if c > so_lon:
        so_lon = c

    so_nho = a
    if b < so_nho:
        so_nho = b
    if c < so_nho:
        so_nho = c

    print("Số lớn nhất là:", so_lon)
    print("Số nhỏ nhất là:", so_nho)

def giai_phong_bac_nhat():
    a = int(input("Nhập hệ số a: "))
    b = int(input("Nhập hệ số b: "))
    c = int(input("Nhập hệ số c: "))
    delta = (b**2) - 4*(a*c)

    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        x = -b / (2*a)
        print("Phương trình có nghiệm kép x =", x)
    else:
        x1 = (-b - delta**0.5) / (2*a)
        x2 = (-b + delta**0.5) / (2*a)
        print("Phương trình có hai nghiệm phân biệt x1 =", x1, "và x2 =", x2)

if __name__ == "__main__":
    tim_max_min()
    giai_phong_bac_nhat()

