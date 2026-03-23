ds_chuoi = []
for i in range(5):
    chuoi = input(f"  Chuỗi {i + 1}: ")
    ds_chuoi.append(chuoi)
for i in range(1, len(ds_chuoi)):
    phan_tu_hien_tai = ds_chuoi[i]
    j = i - 1
    while j >= 0 and len(ds_chuoi[j]) < len(phan_tu_hien_tai):
        ds_chuoi[j + 1] = ds_chuoi[j]
        j -= 1
    ds_chuoi[j + 1] = phan_tu_hien_tai
    print(f"Bước {i}: {ds_chuoi}")
