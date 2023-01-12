import numpy as np
import matplotlib.pyplot as plt
import os
import random

LL = -3
UL = 3
n = np.arange(LL, UL + 1)
xn = np.array([3, 11, 7, 0, -1, 4, 2])
w = np.random.normal(0, 1, size=len(xn))
# yn = [xn[i - 2 - LL] + w[i - LL] for i in n]
yn = np.roll(xn, -2) + w # shift x by 2 and add noise
r = np.correlate(xn, yn, mode='full')

plt.stem(r)
plt.grid()
plt.title('Q7_A')
plt.xlabel('n')
plt.ylabel('r[n]')
plt.yticks()
plt.show()
plt.savefig('Q7_A.png', dpi=100)

## Q7_B
# yn = [xn[i - 4 - LL] + w[i - LL] for i in n]
yn = np.roll(xn, -4) + w # shift x by 2 and add noise
r = np.correlate(xn, yn, mode='full')
plt.stem(r)
plt.grid()
plt.title('Q7_B')
plt.xlabel('n')
plt.ylabel('r[n]')
plt.yticks()
plt.show()
plt.savefig('Q7_B.png', dpi=100)
