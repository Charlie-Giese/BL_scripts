
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


names=["DM", "Duration", "time", "S/N", "length"]
data=pd.read_csv("SMC021_008D1.pls", sep='\s+', skiprows=1, names=names) 
DM=data["DM"].values
time=(data["time"].values)/1000
SN=data["S/N"].values
width=2**(data["Duration"].values)
pul=ax1.scatter(time, DM,
s=width/500, c=(SN-10), cmap="plasma",
vmin=np.min(SN-10), vmax=np.max(SN-10))


ax1.set_xlabel("time (s)")
ax1.set_ylabel("DM (pc/cc)")
ax1.set_xlim(5661.5,5662.5)
#ax1.set_ylim(400, 500)
ax1.set_title("d_zoom")
cbar=fig1.colorbar(pul)
cbar.set_label("S/N")
plt.savefig("zoom_6.png")
#plt.show()



