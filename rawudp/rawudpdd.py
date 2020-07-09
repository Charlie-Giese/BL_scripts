#! usr/bin/python3


import numpy as np
import matplotlib.pyplot as plt
import os
import sys

#file for incoherently dedispersing rawudp files

#stokesI=np.load("1936_I.npy") #format is t1c1, t1c2, t1c3........t1c488, t2c1......
#stokesQ=np.load("1936_Q.npy") #basically filterbank but without header
#stokesU=np.load("1936_U.npy")
stokesV=np.load("1936_V.npy")

file=stokesV
max_freq=197.55855375 #central freq of maximum freq channel
min_freq=102.4414063 #central freq of minimum freq channel
nchans=file.shape[1] #number of frequency channels
DM=56.77 #DM of source

Td_unit_factor=4148 #factor for MHz or GHz
samples_per_sec=195312.5 #factor to get time delay in the right units
tsamples=file.shape[0] #number of time samples

freqs=np.linspace(min_freq, max_freq, nchans)
min_freqs=np.full(np.shape(freqs), min_freq) 
tdelays=((DM*Td_unit_factor/np.square(freqs))*samples_per_sec).astype(np.int32)
tdelays=tdelays-((DM*Td_unit_factor/np.square(max_freq))*samples_per_sec).astype(np.int32)

temp_array=np.zeros(shape=(tsamples-tdelays[nchans-1], nchans), dtype=np.int32)
for i in range(nchans):
    temp_array[:tsamples-tdelays[i] , i ]=file[tdelays[i]: , i]

intensities=np.sum(temp_array, axis=1)
#np.delete(intensities, obj=slice(tsamples-tdelays[0], tsamples, 1), axis=0)

#summed=np.cumsum(intensities, axis=0)
#factor=48
#decimated=summed[factor::factor]-summed[:len(summed)-48:factor]

temp_list=[]
step=int(tsamples/48)
chunk=48
for i in range(step):
    temp=np.sum(intensities[i*chunk : (i+1)*chunk])
    temp_list.append(temp)
decimated=np.array(temp_list)
time=np.arange(0, step, 1)
#fig1=plt.figure(2)
#ax1=fig1.add_subplot(111)
#im=ax1.imshow(temp_array, cmap="viridis", aspect="auto", vmin=np.min(temp_array),
#vmax=np.max(temp_array))
#cbar=plt.colorbar(im)
#cbar.set_label("Intensity")
#ax1.set_xlabel=("Freq")
#ax1.set_ylbael=("Time")
#ax1.set_xlim(400, 488)
#ax1.set_title=("Stokes I")
#plt.savefig("pulse_test1.png")


fig2=plt.figure(2, figsize=(12, 8))
ax2=fig2.add_subplot(111)
ax2.plot(time, decimated)
#ax2.set_xlim(100000, 125000)
ax2.set_title("Stokes V")
ax2.set_xlabel("Time")
ax2.set_ylabel("Intensity")
plt.savefig("1936pulseV.png")

