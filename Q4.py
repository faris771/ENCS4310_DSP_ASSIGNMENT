import matplotlib.pyplot as plt
import numpy as np

nx = np.arange(-3, 3 + 1)
nh = np.arange(-1, 4 + 1)

xn = np.array([3, 11, 7, 0, -1, 4, 2])

hn = np.array([2, 3, 0, -5, 2, 1])

ny = np.arange(-4, 7 + 1)

# find y[n]
yn = np.convolve(xn, hn, 'full')

# plot y[n]
plt.stem(yn)
plt.grid()
plt.title('Q4')
plt.xlabel('n')
plt.ylabel('y[n]')
# plt.savefig('Q4.png', dpi=100)
plt.show()
