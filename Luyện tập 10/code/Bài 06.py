chuoi = input("Nhập chuỗi: ")
dao = ""
for i in range(len(chuoi) - 1, -1, -1):
    dao += chuoi[i]
print(dao)