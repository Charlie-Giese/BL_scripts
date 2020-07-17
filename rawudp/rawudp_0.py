
#! usr/bin/python3


import numpy as np
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

file0=file0.reshape(-1, 488)
file1=file1.reshape(-1, 488)
file2=file2.reshape(-1, 488)
file3=file3.reshape(-1, 488)

stokesI=np.empty_like(file0, dtype=np.int32)
chunksize=int(stokesI.shape[0] / 256)
for i in range(256):
    stokesI[i*chunksize:(i+1)*chunksize] =(
    np.square(file0[i * chunksize: (i+1) * chunksize, :].astype(np.int32)) +
    np.square(file1[i * chunksize: (i+1) * chunksize, :].astype(np.int32)) +
    np.square(file2[i * chunksize: (i+1) * chunksize, :].astype(np.int32)) +
    np.square(file3[i * chunksize: (i+1) * chunksize, :].astype(np.int32)))

mean_list=[]
chan_list=[]
for i in range(488):
    chan=stokesI[:, i]
    temp=np.mean(chan, axis=0)
    mean_list.append(temp)
    chan_list.append(i)
means=np.array(mean_list)
indices=np.argwhere(means >= 100)



stokesI[:,indices ]=0
stokesI[:,[356,462,463,465]]=0
np.save("1936I.npy", stokesI.astype(np.float32))

#stokesI.astype(np.float32).tofile("1936I_rmrfi.fil")



