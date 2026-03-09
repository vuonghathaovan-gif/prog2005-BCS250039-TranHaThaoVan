def bai_1():
    print(" Bài 1")
    pass

def bai_2():
    print("Bài 2")
    pass

def bai_3():
    print("Bài 3")
    pass

def bai_4():
    print("Bài 4")
    pass

def thoat():
    print(" Thoát!")

def main():
    while True:
        menu = ["Bài 1", "Bài 2", "Bài 3", "Bài 4", "Thoát"]
        for i, item in enumerate(menu):
            print(f"{i+1}. {item}")

        try:
            chon = int(input("Chọn chương trình (gõ số tương ứng): "))
            if 1 <= chon <= len(menu):
                selected_program = menu[chon - 1]
                if selected_program == "Bài 1":
                    bai_1()
                elif selected_program == "Bài 2":
                    bai_2()
                elif selected_program == "Bài 3":
                    bai_3()
                elif selected_program == "Bài 4":
                    bai_4()
                elif selected_program == "Thoát":
                    thoat()
            else:
                print("Lỗi")
        except ValueError:
            print("Vui lòng nhập một số!")

if __name__ == "__main__":
    main()