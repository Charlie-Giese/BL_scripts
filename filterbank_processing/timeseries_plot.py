
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


names=["Time", "S/N"]
data=pd.read_csv(sys.argv[1], sep='\s+', skiprows=1, names=names) 
time=data["Time"].values
SN=data["S/N"].values

#rolling mean
#N=5
#SN2=np.zeros_like(SN)
#for i in range(SN.size):
 #   SN2[i]=np.sum(SN[i-N:i+N])/(2*N + 1)

pul=ax1.plot(time, SN)
ax1.set_xlabel("Time (s)")
#ax1.set_xlim(0, 5)
#ax1.set_ylim(15000, 22000)
ax1.set_ylabel("S/N)")
ax1.set_title("1936_I Timeseries")
plt.savefig("ts_1936I_rmrfi.png")

