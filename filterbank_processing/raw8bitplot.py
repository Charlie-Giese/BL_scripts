


import numpy as np 
import matplotlib.pyplot as plt 
import csv
import pandas as pd 
import sys
import os
from matplotlib import colors

fig1=plt.figure(1)
ax1=fig1.add_subplot(111)


names=["time", "channel", "Amp"]
data=pd.read_csv(sys.argv[1], sep='\s+', skiprows=1, names=names)
tim=data["time"].values
freq=np.flip(data["channel"].values)
amp=data["Amp"].values
plot=ax1.scatter(tim, freq,
c=(amp), cmap="viridis",
vmin=np.min(amp), vmax=np.max(amp))
ax1.set_xlabel("Time")
ax1.set_ylabel("Frequency")
ax1.set_title('Lorimer Burst Pulse (Beam 6)')
cbar=fig1.colorbar(plot)
cbar.set_label("S/N")
plt.savefig(sys.argv[2])




