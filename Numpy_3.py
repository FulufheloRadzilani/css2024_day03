# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 15:51:31 2024

@author: radzi
"""

import numpy as np
import matplotlib.pyplot as plt

n = 10
x = np.random.uniform(size=n)
y = np.random.uniform(size=n)
print(sum(x*x+y*y<=1)/n*4)
plt.plot(x[x*x+y*y<=1], y[x*x+y*y<=1], "bo")
plt.plot(x[x*x+y*y>1], y[x*x+y*y>1], "ro")
plt.title("calculating $\pi$")
plt.savefig("pi.jpg")
plt.show()
