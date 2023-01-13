import numpy as np
import matplotlib.pyplot as plt
import os
import random
import scipy as scp
from scipy.signal import lfilter, lfilter_zi

LL = 0
UL = 100
n = np.arange(0, UL + 1)

xn = np.cos(np.pi * n / 2)
yn = np.exp(1j*np.pi*n/4) * xn
w = np.linspace(-2*np.pi, 2*np.pi, 401)
X_ejw = np.fft.fft(xn, len(w))
Y_ejw = np.fft.fft(yn, len(w))

angle = np.angle(X_ejw)
plt.grid()
plt.title('Phase')
plt.xlabel('w')
plt.subplot(2, 1, 1)
plt.plot(w, angle)


mag = np.abs(X_ejw)
plt.grid()
plt.xlabel('w')
plt.title('Magnitude')
plt.subplot(2, 1, 2)
plt.plot(w, mag)
plt.show()

angley = np.angle(Y_ejw)
plt.grid()
plt.title('Phase')
plt.xlabel('w')
plt.subplot(2, 1, 1)
plt.plot(w, angley)

magy = np.abs(Y_ejw)
plt.grid()
plt.xlabel('w')
plt.title('Magnitude')
plt.subplot(2, 1, 2)
plt.xticks()
plt.plot(w, magy)
plt.show()

