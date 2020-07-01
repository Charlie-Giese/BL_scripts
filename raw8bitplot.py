


import numpy as np 
import matplotlib.pyplot as plt 
import csv
import pandas as pd 
import sys
import os
from matplotlib import colors

fig1=plt.figure(1)
ax1=fig1.add_subplot(111)


#for file in os.listdir():
	#filename = os.fsdecode(file)
	#if filename.endswith(".pls"):
names=["time", "channel", "Amp"]
data=pd.read_csv("D8bit_plot.ascii", sep='\s+', skiprows=1, names=names)
tim=data["time"].values
freq=data["channel"].values
amp=data["Amp"].values
plot=ax1.scatter(tim, freq,
c=(amp), cmap="viridis",
vmin=np.min(amp), vmax=np.max(amp))
ax1.set_xlabel("Time")
ax1.set_ylabel("Frequency")
ax1.set_title("Beam D Data")
cbar=fig1.colorbar(plot)
cbar.set_label("S/N")
plt.savefig("BeamDData")
#plt.show()



