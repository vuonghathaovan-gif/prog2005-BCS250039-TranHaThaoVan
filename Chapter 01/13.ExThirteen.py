try:
    a = int(input("Nhập số thứ nhất: "))
    b = int(input("Nhập số thứ hai: "))
    ket_qua = a / b
    print("Kết quả phép chia:", ket_qua)
except ZeroDivisionError:
    print(" Không thể chia cho 0")
except ValueError:
    print("Dữ liệu nhập vào không hợp lệ")