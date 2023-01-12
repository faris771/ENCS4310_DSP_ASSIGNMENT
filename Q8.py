import numpy as np
import matplotlib.pyplot as plt
import os
import random
import scipy as scp
from scipy.signal import lfilter, lfilter_zi


def unit_impulse(interval, a) -> list:  # returns a list
    unit = []
    for sample in interval:
        if sample == -a:
            unit.append(1)
        else:
            unit.append(0)
    return unit

n = [i for i in range(-5, 120 + 1, 5)]
xn = unit_impulse(n, 0)

ak = [1,-1,0.9]
bk = [1]
yn = lfilter(b=bk, a=ak, x=xn)
plt.stem(yn)
plt.grid()
plt.show()
