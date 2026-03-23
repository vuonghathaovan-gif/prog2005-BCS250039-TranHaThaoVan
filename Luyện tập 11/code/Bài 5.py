dictt = {"ten": "Van", "truong": "CMC", "khoa": "CNTTVTT"}
tim_key = input("Nhập key cần kiểm tra: ")
if tim_key in dictt:
    print(f"Key '{tim_key}' có tồn tại.")
else:
    print(f"Key '{tim_key}' không tồn tại.")