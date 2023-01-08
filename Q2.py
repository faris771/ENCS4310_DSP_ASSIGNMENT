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

plt.subplot(3, 1, 1)
plt.stem(na, gna)
plt.grid()
plt.title('A')
plt.ylabel('g[n]')


plt.subplot(3, 1, 2)
plt.stem(nb, gnb)
plt.grid()
plt.title('B')
plt.ylabel('g[n]')


plt.subplot(3, 1, 3)
plt.stem(nc, gnc)
plt.grid()
plt.title('C')

plt.xlabel('n')
plt.ylabel('g[n]')

# plt.savefig("q1_C.png")
# plt.subplot()
plt.subplots_adjust(top=0.9)
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
plt.savefig('Q2.png',dpi=100)


plt.show()
