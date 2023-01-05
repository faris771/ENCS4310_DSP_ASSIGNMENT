"""
AUTHOR: FARIS ABUFARHA
ID: 1200546

"""

import matplotlib.pyplot as plt
import numpy as np



# Q1_B
LL = 0  # UPPER LIMIT
UL = 50  # LOWER LIMIT

n = np.arange(LL, UL + 1)
mean = 0
variance = 1
sigma = np.sqrt(variance)
w = np.random.normal(mean, sigma, size=len(n))

print(w)

y = [(0.04 * np.pi * i + 0.2 * w[i]) for i in n]  # APPENDING EACH VALUE OF y[i] into to the list y

plt.grid()
plt.stem(n, y)
plt.xlabel('n')
# plt.xticks(n)
plt.ylabel('y[n]')
plt.title('Discrete-time signal y[n]')
plt.savefig("q1_B.png")
plt.show()
