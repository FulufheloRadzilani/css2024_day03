# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 10:08:14 2024

@author: radzi
"""

#Plotting graphs using matplotlib

import matplotlib.pyplot as plt

react_conv = [0.5, 0.6, 0.7, 0.7, 0.9]
temp = [180, 200, 220, 240, 260]

#plt.plot(temp, react_conv)
#plt.xlabel("temperature")
#plt.ylabel("reaction conversion")
#plt.title("chemical experiment")
#plt.show()

day1_attendees = [70, 20, 64, 90, 80]
day1_names = ["Blessing", "Mali", "Pangi", "Tafi", "Shini"]

#plt.bar(day1_names,day1_attendees)
#plt.xlabel("attendees")
#plt.ylabel("attendence")
#plt.title("Day 1 data")
#plt.show()

x_scatter = [1, 2, 3, 4, 5]
y_scatter = [2, 4, 6, 8, 10]

plt.scatter(x_scatter, y_scatter)
plt.show()

x_histogram