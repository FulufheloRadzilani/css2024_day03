# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 12:22:01 2024

@author: radzi
"""

import pandas as FR
#from ydata_profiling import ProfileReport

df = FR.read_csv("C:/Users/radzi/Downloads/CSS/data_02/iris.csv")
profile = ProfileReport(df, title="Profiling Report")
profile.to_fie("your_report.html")
