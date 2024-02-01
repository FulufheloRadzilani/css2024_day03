# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 11:50:24 2024

@author: radzi
"""

import pandas as FR
import matplotlib.pyplot as plt

#Plotting three curves oin one sketch

df = FR.read_csv("poker_2016_09_27.csv", names=["Time", "NUN", "x", "y", "z"])

df["Time"] = FR.to_datetime(df["Time"], format = "%H:%M:%S").dt.time
plt.plot(df["Time"], df["x"], label = "x")
plt.plot(df["Time"], df["y"], label = "y")
plt.plot(df["Time"], df["z"], label = "z")

plt.plot(df["Time"], y=["x", "y", "z"])
plt.show()
