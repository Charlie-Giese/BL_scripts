
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
data=pd.read_csv(sys.argv[1], sep='\s+', skiprows=1, names=names)
WFplot_1936I_rmrfi_pulse2.pngDM=data["DM"].values
time=(data["time"].values)*(163.84*(10**(-6)))
SN=data["S/N"].values
width=2**(data["Duration"].values)

print(time)

pul=ax1.scatter(time, SN, s=SN)
ax1.set_xlim(0, 5)
ax1.set_xlabel("time (s)")
ax1.set_ylabel("SN")
ax1.set_title("1936I Pulse Search")
#cbar=fig1.colorbar(pul)
#cbar.set_label("S/N")
plt.savefig("1936I_pulsesearch.png")
#plt.show()



