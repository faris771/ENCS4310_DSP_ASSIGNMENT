import numpy as np
import matplotlib.pyplot as plt
import os
import random
import scipy as scp
from scipy.signal import lfilter, lfilter_zi


delta = np.concatenate((np.array([5]),np.zeros(80)))
plt.stem(delta)
plt.grid()
plt.show()