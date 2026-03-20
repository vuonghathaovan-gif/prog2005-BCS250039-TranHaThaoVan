ds = []
for i in range(5):
    s = input("Nhập chuỗi " + str(i + 1) + ": ")
    ds.append(s)

for i in range(len(ds) - 1):
    for j in range(len(ds) - 1 - i):
        if len(ds[j]) < len(ds[j + 1]):
            tam = ds[j]
            ds[j] = ds[j + 1]
            ds[j + 1] = tam
    print("Bước", i + 1, ":", ds)

print(ds)