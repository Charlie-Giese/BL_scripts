import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import pandas as pd

fig2=plt.figure(2)
ax2=fig2.add_subplot(111)


names=["freq", "S/N"]
data=pd.read_csv(sys.argv[1]+'.ascii', sep='\s+', skiprows=0, names=names)
SN=data["S/N"].values

freq=data['freq'].values
pul2=ax2.plot(freq, SN)
ax2.set_xlabel("Freq channel")
#ax2.set_xlim(500, 67000)
ax2.set_ylabel("S/N)")
ax2.set_title(sys.argv[1])
plt.savefig(sys.argv[1]+'.png')
