
import numpy as np
from matplotlib import pyplot as plt


def calculate(n):
    constant = 1 + (1/n)
    constant = pow(constant, n)
    return constant

arr = list()

for i in range(1,100):
    arr.append(calculate(i))

arr = np.array(arr)

plt.plot(arr)
plt.show()
