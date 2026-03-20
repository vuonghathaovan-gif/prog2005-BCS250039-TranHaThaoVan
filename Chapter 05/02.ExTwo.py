import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-5, 5, 100)
y1 = x ** 2
y2 = x ** 3
plt.plot(x, y1, color='blue', label='y = x²')
plt.plot(x, y2, color='red', label='y = x³')
plt.title('Đồ thị hàm số y = x² và y = x³')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()