"""
AUTHOR: FARIS ABUFARHA
ID: 1200546

"""

import matplotlib.pyplot as plt
import numpy as np


#  δ(n - a )   a: delay or advance
def unit_impulse(interval, a) -> list:  # returns a list
    unit = []
    for sample in interval:
        if sample == -a:
            unit.append(1)
        else:
            unit.append(0)
    return unit


LL = -5
UL = 5
n = np.arange(LL, UL + 1)
x1 = unit_impulse(n, 2)
x2 = unit_impulse(n, -4)
x = []
for i in range(len(x1)):
    x.append(2 * x1[i] - x2[i])

plt.grid()
plt.stem(n, x)
plt.xlabel('n')
plt.xticks(n)
plt.ylabel('x[n]')
plt.savefig("q1_a.png")
plt.show()
