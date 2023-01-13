import numpy as np
import matplotlib.pyplot as plt
import os
import random
import scipy as scp
from scipy.signal import lfilter, lfilter_zi


#  δ(n - a )   a: delay or advance
def unit_impulse(interval, a) -> list:  # returns a list
    unit = []
    for sample in interval:
        if sample == -a:
            unit.append(1)
        else:
            unit.append(0)
    return unit


def unit_step(interval, delay) -> list:
    unit = []
    for sample in interval:
        if sample >= -delay:
            unit.append(1)
        else:
            unit.append(0)

    return unit

LL = -5
UL = 30
n = np.arange(LL, UL + 1)
rec = [5 * (unit_step(n, 0)[i - LL] - unit_step(n, -20)[i- LL]) for i in n]

plt.stem(n, rec)
plt.grid()
plt.show()
plt.savefig('Q9_A.png')

yn = rec - np.roll(rec, +1) # ask about this

plt.stem(n, yn)
plt.grid()
plt.show()

# b

trig = [i * (unit_step(n, 0)[i- LL] - unit_step(n, -10)[i- LL]) + (20 - i) * (unit_step(n, -10)[i- LL] - unit_step(n, -20)[i- LL]) for i
        in n]
plt.stem(n, trig)
plt.grid()
plt.show()
plt.savefig('Q9_B.png')
yn = trig - np.roll(trig, 1) # ask about this
plt.stem( yn)
plt.grid()
plt.show()

# c
LL = 0
UL = 100
n = np.arange(LL, UL + 1)
sinus = [np.sin(np.pi * i / 25) * (unit_step(n, 0)[i- LL] - unit_step(n, -100)[i- LL]) for i in n]
plt.stem(n, sinus)
plt.grid()
plt.show()

yn = sinus - np.roll(sinus, 1) # ask about this
plt.stem(n, yn)
plt.grid()
plt.show()



