
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

stokesI=np.load("1936I_rmrfi.npy")



chunk=64
step=int(stokesI.shape[0]/chunk)
decimated=np.zeros(shape=(step, stokesI.shape[1]))
for i in range(step):
    decimated[i, :]=np.sum(stokesI[i*chunk : (i+1)*chunk, :], axis=0)

stokesI=decimated[int(2246000/chunk) :int(2247000/chunk)  , :]

im=ax1.imshow(stokesI, cmap="viridis", aspect="auto"
,vmin=np.min(stokesI),vmax=np.max(stokesI))
cbar=plt.colorbar(im)
cbar.set_label("Intensity")
plt.savefig("WFplot_1936I_rmrfi_pulse2.png")
