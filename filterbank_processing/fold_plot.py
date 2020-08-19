import numpy as np 
import matplotlib.pyplot as plt 
import csv
import pandas as pd 
import sys
import os
from matplotlib import colors


folded_data=sys.argv[1]

data=pd.read_csv(folded_data+'.ascii', sep='\s+', skiprows=1)

plt.figure(num=1)
intens=data.iloc[:,1].values
bins=np.arange(0, intens.shape[0], 1)
pulse_phase=bins/np.max(bins)
intens=intens+abs(np.min(intens))
normalised=intens/np.max(intens)
plt.xlabel('Pulse Phase')
plt.ylabel('Normalised Amplitude')
plt.title('PSR Pulse Profile')
plt.plot(pulse_phase, normalised)
plt.savefig(folded_data+'.png')
