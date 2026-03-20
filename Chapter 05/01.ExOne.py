import matplotlib.pyplot as plt
xep_loai = ['Xuất sắc', 'Giỏi', 'Trung bình', 'Yếu', 'Kém']
so_luong = [6, 10, 12, 4, 1]
plt.bar(xep_loai, so_luong)
plt.title('Kết quả học tập của lớp')
plt.xlabel('Xếp loại')
plt.ylabel('Số học sinh')
plt.show()