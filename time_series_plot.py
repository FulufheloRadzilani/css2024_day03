# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 11:34:48 2024

@author: radzi
"""

import pandas as FR
import matplotlib.pyplot as plt

#Plotting a pie chart

df = FR.read_csv("C:/Users/radzi/Downloads/CSS/data_02/iris.csv", index_col=0)

print(df.info())

df["Date"]=FR.to_datetime(df["Date"], format="%Y-%m-%d")
print(df.info())

plt.plot(df["Date"], df["Temperature"])
plt.ylabel("temp")
plt.show()

df["Temperature"].plot(kind="hist", bins=20, title="Temperature")
plt.show()