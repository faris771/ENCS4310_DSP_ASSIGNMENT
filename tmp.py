import numpy as np
import matplotlib.pyplot as plt

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

# Define the interval
n = np.arange(-5, 45)

# Define the rectangular pulse x(n)

x = [(unit_step(n, 0)[i + -LL] - unit_step(n, -10)[i +-LL]) for i in n]

# Define the impulse response h[n]
h = (0.9)**n * np.heaviside(n, 1)

# Convolve x(n) and h[n] to find y(n)
y = np.convolve(x, h, mode='full')

# Plot x(n)
plt.subplot(3,1,1)
plt.stem( x)
plt.title('x(n)')

# Plot h[n]
plt.subplot(3,1,2)
plt.stem( h)
plt.title('h[n]')

# Plot y(n)
plt.subplot(3,1,3)
plt.stem(y)
plt.title('y(n)')
plt.show()
