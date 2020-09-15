
import numpy as np 
import matplotlib.pyplot as plt 
import csv
import pandas as pd 
import sys
import os
from matplotlib import colors

#This code plots a dedispersed timeseries
mean=11.2061
rms=767.005

beta=1.25
t_sys=23 #K
n_pol=2
bw=23.828*10**6 #MHz
t_obs=0.06 #s
gain=1

fig1=plt.figure(1)
ax1=fig1.add_subplot(111)
filename=sys.argv[1]

names=["Time", "S/N"]
data=pd.read_csv(filename+'.ascii', sep='\s+', skiprows=1, names=names) 
time=data["Time"].values
amp=data["S/N"].values
SN=(amp-mean)/rms
factor=beta*t_sys*gain/(n_pol*bw*t_obs)**(0.5)
Jy=SN*factor

pul=ax1.plot(time, SN)
ax1.set_xlabel("Time (s)")
ax1.set_xlim(3.5, 4)
#ax1.set_ylim(15000, 22000)
ax1.set_ylabel("S/N)")
ax1.set_title("Crab Giant Pulse")
plt.savefig(filename+".png")

