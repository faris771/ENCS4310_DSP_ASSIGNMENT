import numpy as np
import matplotlib.pyplot as plt
import os
import random
import scipy as scp
from scipy.signal import lfilter, lfilter_zi

def unit_step(interval, delay) -> list:
    unit = []
    for sample in interval:
        if sample >= -delay:
            unit.append(1)
        else:
            unit.append(0)

    return unit

def unit_impulse(interval, a) -> list:  # returns a list
    unit = []
    for sample in interval:
        if sample == -a:
            unit.append(1)
        else:
            unit.append(0)
    return unit


# n = [i for i in range(-5, 120 + 1)]
n = np.arange(-5, 120 + 1)

xn = unit_impulse(n, 0)

ak = [1, -1, 0.9]
bk = [1]
hn = lfilter(b=bk, a=ak, x=xn)
plt.stem(n,hn)
plt.grid()
plt.savefig('Q8_A.png')
plt.show() # ok

#b
xn = unit_step(n, 0)
sn= lfilter(b=bk, a=ak, x=xn)
plt.stem(n, sn)
plt.grid()
plt.savefig('Q8_B.png')
plt.show()


#c
#check if hn is stable or not

rts = np.roots(hn)
if all(abs(rts) < 1):
    print("System is stable")
else:
    print("System is not stable")





