"""
AUTHOR: FARIS ABUFARHA
ID: 1200546

"""

import matplotlib.pyplot as plt
import numpy as np

# Q1_C
LL = -10  # UPPER LIMIT
UL = 9  # LOWER LIMIT
n = np.arange(LL, UL + 1)
z = [5 - i % 5 for i in n]


plt.grid()
plt.stem(n, z)
plt.xlabel('n')
plt.xticks(n)
plt.ylabel('Z[n]')
plt.title('Q1_C')
plt.savefig("q1_C.png")
plt.show()
