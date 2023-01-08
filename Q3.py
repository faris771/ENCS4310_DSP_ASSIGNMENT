
import matplotlib.pyplot as plt
import numpy as np

LL = -10
UL = 10
n = np.arange(LL, UL + 1)
x = np.exp((-0.1 + 1j * 0.3) * n)

# Plot the magnitude of x[n]
plt.subplot(2, 2, 1)
plt.stem(n, np.abs(x))
plt.title('Magnitude')
plt.grid()

# Plot the phase of x[n]
plt.subplot(2, 2, 2)
plt.stem(n, np.angle(x))
plt.title('Phase')
plt.grid()

# Plot the real part of x[n]
plt.subplot(2, 2, 3)
plt.stem(n, np.real(x))
plt.title('Real Part')
plt.grid()
# Plot the imaginary part of x[n]
plt.subplot(2, 2, 4)
plt.stem(n, np.imag(x))
plt.title('Imaginary Part')
plt.grid()

# to change plot dimensions
plt.subplots_adjust(top=0.9)
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
plt.savefig('Q3.png',dpi=100)


plt.show()
