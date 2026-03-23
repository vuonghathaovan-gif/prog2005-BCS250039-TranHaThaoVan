nhap = input("Nhập (cách nhau bằng dấu cách): ")
cac_phan_tu = nhap.split()
ds_so = []
for phan_tu in cac_phan_tu:
    so = int(phan_tu)
    ds_so.append(so)

ds_so_chan = []
for so in ds_so:
    if so % 2 == 0:
        ds_so_chan.append(so)

if len(ds_so_chan) == 0:
    print("Không có.")
else:
    print(f"Số chẵn: {ds_so_chan}")
    tong = 0
    for so in ds_so_chan:
        tong += so
    print(f"Tổng: {tong}")