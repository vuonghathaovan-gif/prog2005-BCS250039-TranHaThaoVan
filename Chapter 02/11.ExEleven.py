score = float(input("Nhập điểm trung bình: "))

if score >= 8:
    print("Giỏi")
elif 6.5 <= score < 8:
    print("Khá")
elif 5.0 <= score < 6.5:
    print("Trung bình")
else:
    print("Yếu")
