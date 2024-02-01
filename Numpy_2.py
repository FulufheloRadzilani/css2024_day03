# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 15:25:40 2024

@author: radzi
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("noisydata.csv", skiprows=1,delimiter=",")
data_avg = np.mean(data,0)
print("average of columns:")
print(data_avg[1])
pressure = data[:,0]
flowrate = data[:,1]
#the number 3 is the exponet (shape of the graph)
fit = np.polyfit(pressure,flowrate,3)
flowfit = np.polyval(fit,pressure)
plt.plot(pressure,flowrate,"go")
plt.plot(pressure,flowfit,"k")
plt.xlabel("pressure(pa)")
plt.ylabel("flow rate ($m^3/s$")
plt.show()