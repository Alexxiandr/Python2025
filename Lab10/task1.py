import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 500)

y = np.sin(5 * x) / x
y[np.isnan(y)] = 5

plt.plot(x, y, color='red', linewidth=3, linestyle='-', label='Y = sin(5x)/x')
plt.title('Графік функції Y(x) = sin(5x)/x', fontsize=14)
plt.xlabel('x', fontsize=12, color='black')
plt.ylabel('Y(x)', fontsize=12, color='black')

plt.legend()
plt.grid(True)
plt.show()