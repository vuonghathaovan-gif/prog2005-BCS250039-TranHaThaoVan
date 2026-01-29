# Định nghĩa hàm greet với đối số mặc định
def greet(name="Student"):
    print("Hello,", name + "!")

ten = input("Nhập tên của bạn (Enter để bỏ qua): ")

if ten:
    greet(ten)
else:
    greet()

