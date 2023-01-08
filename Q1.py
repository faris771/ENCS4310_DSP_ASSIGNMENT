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

y = [np.cos(0.04 * np.pi * t) + 0.2 * w[t] for t in n]  # APPENDING EACH VALUE OF y[i] into to the list y

plt.grid() # TO SHOW THE GRID
plt.stem(n, y) # TO PLOT THE GRAPH in discrete form
plt.xlabel('n')
# plt.xticks(n)
plt.ylabel('y[n]')
plt.title('Q1_B')
plt.savefig("q1_B.png") # SAVING THE PLOT AS A PNG FILE
plt.show()
