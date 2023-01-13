import numpy as np
import matplotlib.pyplot as plt

# Define the input sequence
x = np.zeros(100)
x[:20] = 5

# Implement the differentiator
y = np.zeros(100)
y[1:] = x[1:] - x[:-1]

# Plot the input and output sequences
plt.figure()
plt.stem(x)
plt.title("Input sequence (rectangular pulse)")

plt.figure()
plt.stem(y)
plt.title("Output sequence (simple differentiator)")
plt.show()
