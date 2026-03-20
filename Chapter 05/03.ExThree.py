import matplotlib.pyplot as plt
san_pham = ['A', 'B', 'C', 'D', 'E']
doanh_so = [30, 25, 15, 20, 10]
plt.pie(doanh_so, labels=san_pham, autopct='%1.1f%%')
plt.title('Doanh số của 5 sản phẩm')
plt.show()