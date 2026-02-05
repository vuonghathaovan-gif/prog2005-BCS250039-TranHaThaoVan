num = int(input("Nhập một số: "))
tong = 0
for chu_so in str(abs(num)):  
    tong += int(chu_so)

print(f"Tổng các chữ số của {num} là {tong}.")
