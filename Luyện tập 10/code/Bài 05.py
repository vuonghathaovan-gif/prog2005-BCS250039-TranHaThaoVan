import matplotlib.pyplot as plt
import math
x1, y1 = [], []
x = -10
while x <= 10:
    x1.append(x)
    y1.append(x ** 2)
    x += 0.1
x2, y2 = [], []
x = 0
while x <= 10:
    x2.append(x)
    y2.append(math.sqrt(x))
    x += 0.1
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(x1, y1)
ax1.set_title("y = x^2")
ax1.set_xlabel("x")
ax1.set_ylabel("y")

ax2.plot(x2, y2)
ax2.set_title("y = sqrt(x)")
ax2.set_xlabel("x")
ax2.set_ylabel("y")

plt.tight_layout()
plt.show()