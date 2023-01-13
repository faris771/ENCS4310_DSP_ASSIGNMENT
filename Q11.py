import numpy as np
import matplotlib.pyplot as plt
import os
import random
import scipy as scp
from scipy.signal import lfilter, lfilter_zi

# Define the sequence x[n]
x = np.array([1, -0.5, -0.3, -0.1])

# Compute the discrete-time Fourier transform of x[n] at 501 equispaced frequencies between [0,π]
frequencies = np.linspace(0, np.pi, 501)
X = np.fft.fft(x, len(frequencies))

print(X)
##

# Plot the magnitude of X(e^jw)
plt.figure()
plt.plot(frequencies, np.abs(X))
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('Magnitude')
plt.title('Magnitude of X(e^jw)')

# Plot the angle of X(e^jw)
plt.figure()
plt.plot(frequencies, np.angle(X))
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('Angle (rad)')
plt.title('Angle of X(e^jw)')
plt.show()

# Plot the real part of X(e^jw)
plt.figure()
plt.plot(frequencies, np.real(X))
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('Real')
plt.title('Real part of X(e^jw)')
plt.show()

# Plot the imaginary part of X(e^jw)
plt.figure()
plt.plot(frequencies, np.imag(X))
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('Imaginary')
plt.title('Imaginary part of X(e^jw)')
plt.show()