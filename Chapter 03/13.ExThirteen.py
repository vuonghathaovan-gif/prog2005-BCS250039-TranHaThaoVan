def kiem_tra_palindrome(chuoi):
    chuoi_chuan = chuoi.lower().replace(" ", "")
    return chuoi_chuan == chuoi_chuan[::-1]
chuoi = input("Nhập chuỗi cần kiểm tra: ")
if kiem_tra_palindrome(chuoi):
    print(f'"{chuoi}" Là Palindrome ')
else:
    print(f'"{chuoi}" Không là Palindrome ')
