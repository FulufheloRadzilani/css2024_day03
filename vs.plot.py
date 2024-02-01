# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 10:41:29 2024

@author: radzi
"""

import pandas
import matplotlib.pyplot as plt

#Plotting a scatter plot

file = pandas.read_csv("C:/Users/radzi/Downloads/CSS/data_02/iris.csv")

file ["class"] = file ["class"].str.replace("Iris-", "")

#plt.scatter(file["sepal_length"], file["sepal_width"])
#plt.xlabel("sepal_length")
#plt.ylabel("sepal_width")
#plt.show()

#import seaborn as sbn
#sbn.pairlot(file, hue="class")
#plt.show()

class_count = file["class"].value_counts()
plt.pie(class_count)
plt.show()
