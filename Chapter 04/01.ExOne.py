def xu_ly_tuple(numbers):
    tong = sum(numbers)
    lon_nhat = max(numbers)
    nho_nhat = min(numbers)
    return tong, lon_nhat, nho_nhat

numbers = (3, 1, 7, 4, 9, 2)
tong, lon_nhat, nho_nhat = xu_ly_tuple(numbers)
print(f"Tuple: {numbers}")
print(f"Tổng: {tong}")
print(f"Lớn nhất: {lon_nhat}")
print(f"Nhỏ nhất: {nho_nhat}")