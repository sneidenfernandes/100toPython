import matplotlib.pyplot as plt
import numpy as np 
from sklearn.linear_model import LinearRegression
import random 

x_values = []
y_values = []

reg = LinearRegression

for i in range(1000):
    x_values.append(random.randint(0,100))
    y_values.append(random.randint(0,100))

  

    x = np.array(x_values)
    x = x.reshape(-1,1)

    y = np.array(y_values)
    y = y.reshape(-1,1)

    if i % 5 == 0:
        reg.fit(x,y)
        plt.xlim(0,100)
        plt.ylim(0,100)
        plt.scatter(x_values, y_values, color='black')
        plt.pause(0.001)


plt.show()
