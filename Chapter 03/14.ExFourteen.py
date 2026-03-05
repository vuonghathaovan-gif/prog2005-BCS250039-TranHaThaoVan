def count_vowels(s):
    nguyen_am = "aeiouAEIOU"
    dem = 0
    for ky_tu in s:
        if ky_tu in nguyen_am:
            dem += 1
    return dem

chuoi = input("Nhập chuỗi: ")
print(f'Số nguyên âm trong "{chuoi}": {count_vowels(chuoi)}')
