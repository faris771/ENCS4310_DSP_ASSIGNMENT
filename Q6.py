import numpy as np
import matplotlib.pyplot as plt


# u(n-5)  interval n, delay -5
def unit_step(interval, delay) -> list:
    unit = []
    for sample in interval:
        if sample >= -delay:
            unit.append(1)
        else:
            unit.append(0)

    return unit


LL = -5
UL = 45
n = np.arange(LL, UL + 1)

xn = [(unit_step(n, 0)[i+ abs(LL)] - unit_step(n, -10)[i+ abs(LL)]) for i in n]
plt.stem(n, xn)
plt.grid()
# plt.savefig('Q6_X.png')
plt.show()

hn = [(unit_step(n, 0)[i + abs(LL)] * (0.9 ** i)) for i in
      n]  # -LL = --5 = + is for the relative index, there's no index -5, but relatively it's same as index 0 for the list
plt.stem(n, hn)
plt.grid()
# plt.savefig('Q6_X.png')
plt.show()

#
#
#
#
