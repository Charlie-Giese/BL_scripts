
import numpy as np 
import matplotlib.pyplot as plt 
import csv
import pandas as pd 
import sys
import os
from matplotlib import colors

#This code plots a dedispersed timeseries

fig1=plt.figure(1)
ax1=fig1.add_subplot(111)
file_name=sys.argv[1]

names=["Time", "S/N"]
data=pd.read_csv(file_name+'.ascii', sep='\s+', skiprows=1, names=names) 
time=data["Time"].values
SN=data["S/N"].values

pul=ax1.plot(time, SN)
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("S/N)")
ax1.set_title(file_name)
plt.savefig(file_name+'timeseries.png')

