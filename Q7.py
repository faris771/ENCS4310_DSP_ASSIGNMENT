import numpy as np
import matplotlib.pyplot as plt
import os
import random

n = np.arange(-3, 3 + 1)
xn = np.array([3, 11, 7, 0, -1, 4, 2])
w = np.random.normal(0, 1, size=len(xn))

yn = [xn[i-2] + w[i] for i in n]
r = np.correlate(xn, yn)
plt.stem(r)
plt.grid()
plt.title('Q7_A')
plt.xlabel('n')
plt.ylabel('r[n]')
plt.yticks()
plt.show()
plt.savefig('Q7_A.png', dpi=100)


## Q7_B
yn = [xn[i-4] + w[i] for i in n]
r = np.correlate(xn, yn)
plt.stem(r)
plt.grid()
plt.title('Q7_B')
plt.xlabel('n')
plt.ylabel('r[n]')
plt.yticks()
plt.show()
plt.savefig('Q7_B.png', dpi=100)



