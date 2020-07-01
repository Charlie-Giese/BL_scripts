


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
DMs=np.linspace(0, 30, 1)


#for file in os.listdir():
	#filename = os.fsdecode(file)
	#if filename.endswith(".pls"):
names=["DM", "Duration", "time", "S/N", "length"]
data=pd.read_csv(sys.argv[1], sep='\s+', skiprows=1, names=names)
index=data[data["S/N"] <= 6].index
data=data.drop(index, inplace=False) 
DM=data["DM"].values
time=(data["time"].values)/1000
SN=data["S/N"].values
width=2**(data["Duration"].values)
#pul=ax1.scatter(time, DM,
#s=width/500, c=(SN), cmap="plasma",
#vmin=np.min(SN), vmax=np.max(SN))
	#	continue
	#else:
	#	continue
ax1.scatter(width, SN)   
ax1.set_ylabel("S/N")
ax1.set_xlabel("width (ms)")
ax1.set_title(sys.argv[1])
#cbar=fig1.colorbar(pul)
#cbar.set_label("S/N")
plt.savefig(sys.argv[2])
#plt.show()



