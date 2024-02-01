# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 12:10:11 2024

@author: radzi
"""

import pandas as FR
import matplotlib.pyplot as plt

df = FR.read_excel("")

print(df.info())

plt.scatter.(df["REFCODE"], df["Activation_Energy(kcal/mol)"])
plt.scatter.