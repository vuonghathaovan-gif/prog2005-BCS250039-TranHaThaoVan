chuoi = input("Nhập chuỗi số (ngăn cách bởi ';'): ")
numbers = [int(x.strip()) for x in chuoi.split(";")]

for num in numbers:
    print(num)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


so_chan = sum(1 for n in numbers if n % 2 == 0)
so_am = sum(1 for n in numbers if n < 0)
so_nguyen_to = sum(1 for n in numbers if is_prime(n))
trung_binh = sum(numbers) / len(numbers)

print(f"Có {so_chan} số chắn")
print(f"Có {so_am} số âm")
print(f"Có {so_nguyen_to} số nguyên tố")
print(f"Trung bình: {trung_binh:.2f}")