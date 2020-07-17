import numpy as np
import matplotlib.pyplot as plt
import os
import sys


fig2=plt.figure(2)
ax2=fig2.add_subplot(111)

names=["freq", "S/N"]
data=pd.read_csv(sys.argv[2], sep='\s+', skiprows=0, names=names)
SN=data["S/N"].values
SN[[356,462,463,465]]=0
freq=np.arange(0, SN.shape[0], 1)
pul2=ax2.plot(freq, SN)
ax2.set_xlabel("Freq channel")
#ax2.set_xlim(350, 370)
ax2.set_ylabel("S/N)")
ax2.set_title("1936I Bandpass")
plt.savefig("bandpass_1936I_rmrfi.png")

