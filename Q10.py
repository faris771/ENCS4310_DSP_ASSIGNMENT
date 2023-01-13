import numpy as np
import matplotlib.pyplot as plt
import os
import random
import scipy as scp
from scipy.signal import lfilter, lfilter_zi

LL = 0
UL = 500
w = np.arange(LL, UL + 1) * np.pi / 500 # 500 samples
X_ejw = np.exp(1j*w) / (np.exp(1j*w) - 0.5*np.ones(UL + 1))


angle = np.angle(X_ejw)
plt.grid()
plt.subplot(2, 2, 4)
plt.title('Phase')
plt.xlabel('w')
plt.plot(w, angle)

real = np.real(X_ejw)
plt.subplot(2, 2, 1)
plt.grid()
plt.title('Real')
plt.xlabel('w')
plt.plot(w, real)

imag = np.imag(X_ejw)
plt.subplot(2, 2,3)
plt.grid()
plt.title('Imaginary')
plt.xlabel('w')
plt.plot(w, imag)

mag = np.abs(X_ejw)
plt.grid()
plt.subplot(2, 2, 2)
plt.title('Magnitude')
plt.xlabel('w')
plt.plot(w, mag)


plt.subplots_adjust(top=0.9)
fig = plt.gcf()
fig.set_size_inches(10, 10)
plt.savefig('Q10.png',dpi=100)
plt.show()

