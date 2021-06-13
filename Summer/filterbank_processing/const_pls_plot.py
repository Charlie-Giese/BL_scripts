
import numpy as np 
import matplotlib.pyplot as plt 
import csv
import pandas as pd 
import sys
import os
from matplotlib import colors

#This code plots DM vs Time with SN being represented by colour

fig1=plt.figure(1)
ax1=fig1.add_subplot(111)

file_name=sys.argv[1]
sample_time=163.84*(10**(-6))

names=["DM", "Duration", "time", "S/N", "length"]
data=pd.read_csv(file_name+'.pls', sep='\s+', skiprows=1, names=names)
DM=data["DM"].values
time=(data["time"].values)*sample_time
SN=data["S/N"].values
width=2**(data["Duration"].values)

print(time)

pul=ax1.scatter(time, SN, s=SN)
ax1.set_xlim(0, 5)
ax1.set_xlabel("time (s)")
ax1.set_ylabel("SN")
ax1.set_title(file_name)
#cbar=fig1.colorbar(pul)
#cbar.set_label("S/N")
plt.savefig(file_name+"pulsesearcs.png")




