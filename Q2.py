"""
AUTHOR: FARIS ABUFARHA
ID: 1200546

"""

import matplotlib.pyplot as plt
import numpy as np

f1 = 5
f2 = 15
na = np.arange(0, 1, 1 / 50)
nb = np.arange(0, 1, 1 / 30)
nc = np.arange(0, 1, 1 / 20)

gna = [(np.cos(2 * np.pi * f1 * t) + 0.125 * np.cos(2 * np.pi * f2 * t)) for t in na]
gnb = [(np.cos(2 * np.pi * f1 * t) + 0.125 * np.cos(2 * np.pi * f2 * t)) for t in nb]
gnc = [(np.cos(2 * np.pi * f1 * t) + 0.125 * np.cos(2 * np.pi * f2 * t)) for t in nc]

plt.grid()


plt.stem(nc, gnc)
plt.stem(nb, gnb)
plt.xlabel('n')
plt.ylabel('g[n]')
plt.title('Q2_A')
# plt.savefig("q1_C.png")
# plt.subplot()


plt.show()
