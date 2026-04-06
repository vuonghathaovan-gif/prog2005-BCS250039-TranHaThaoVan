# Bài 7
sinh_vien = {"A": 8.5, "B": 7.0, "C": 6.5}
def tinh_trung_binh(d):
    return sum(d.values()) / len(d)
print(tinh_trung_binh(sinh_vien))