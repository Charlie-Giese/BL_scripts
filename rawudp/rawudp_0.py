
#! usr/bin/python3


import numpy as np
import matplotlib.pyplot as plt
import os
import sys


#file crab_giant_pulses1_2020-03-17T17:06:12,_17901776.rawudp
path="/mnt/ucc4_data2/data/David/crab_extracted_pulses/"

#file0=open(path+sys.argv[1], 'rb')
#file1=open(path+sys.argv[2], 'rb')
#file2=open(path+sys.argv[3], 'rb')
#file3=open(path+sys.argv[4], 'rb')

file0=open(path+"/crab_giant_pulses0_2020-03-17T19:25:13,_17901936.rawudp", 'rb')
file1=open(path+"/crab_giant_pulses1_2020-03-17T19:25:13,_17901936.rawudp", 'rb')
file2=open(path+"/crab_giant_pulses2_2020-03-17T19:25:13,_17901936.rawudp", 'rb')
file3=open(path+"/crab_giant_pulses3_2020-03-17T19:25:13,_17901936.rawudp", 'rb')

file0=np.fromfile(file0, dtype=np.int8)
file1=np.fromfile(file1, dtype=np.int8)
file2=np.fromfile(file2, dtype=np.int8)
file3=np.fromfile(file3, dtype=np.int8)

#file0=file0.reshape(8203104, 488)
#file1=file1.reshape(8203104, 488)
#file2=file2.reshape(8203104, 488)
#file3=file3.reshape(8203104, 488)

stokesI=np.empty_like(file0, dtype=np.int32)
chunksize=15637167
for i in range(256):
    stokesI[i*chunksize:(i+1)*chunksize] =(
    np.square(file0[i * chunksize: (i+1) * chunksize].astype(np.int32)) +
    np.square(file1[i * chunksize: (i+1) * chunksize].astype(np.int32)) +
    np.square(file2[i * chunksize: (i+1) * chunksize].astype(np.int32)) +
    np.square(file3[i * chunksize: (i+1) * chunksize].astype(np.int32)))

#stokesI=stokesI.reshape(4003114752, )



stokesI.tofile("1936_I.fil", format="%f")



"""
freqs=np.linspace(197.55855375, 102.4414063, 488) #in MHz

def tdelay(freq):
    tdelay=235538.73/(np.square(freq))
    return tdelay #in MHz


for i in range(487):
    file0[:, i]=(file0[:, i+tdelay(freq[i])).astype(np.int32)
    file1[:, i]=(file0[:, i]-tdelay(freq[i])).astype(np.int32)
    file2[:, i]=(file0[:, i]-tdelay(freq[i])).astype(np.int32)
    file3[:, i]=(file0[:, i]-tdelay(freq[i])).astype(np.int32)



im=plt.imshow(stokesI, cmap="viridis", aspect="auto")
plt.title("Stokes I")
cbar=plt.colorbar(im)
cbar.set_label("Stokes I")
plt.xlabel("Freq Channel")
plt.ylabel("Time")
plt.savefig(sys.argv[2])
"""
