mau_sac = ["Red", "Blue", "Green", "Yellow", "Purple"]
print(f"Danh sách ban đầu: {mau_sac}")
try:
    mau_sac.remove("Green")
    print("Đã xóa 'Green'.")
except ValueError:
    print(" 'Green' không có trong danh sách!")
print(f"Danh sách sau khi xóa: {mau_sac}")
