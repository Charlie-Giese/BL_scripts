
#! usr/bin/python3


import numpy as np
import os
import sys


#file crab_giant_pulses1_2020-03-17T17:06:12,_17901776.rawudp
path="/mnt/ucc4_data2/data/David/crab_extracted_pulses/"
#file length is 8203104*488
file_length=488*8203104
N=36621
Nsets=int(file_length/N)

for i in range(Nsets):
    with open(path+"/crab_giant_pulses0_2020-03-17T19:25:13,_17901936.rawudp", "rb") as f:
        map0 = np.memmap(f, mode="r", dtype=np.int8)
        x_real=np.array(map0[i*N:(i+1)*N]).astype(np.int8)
        del map0
    f.close()
    with open(path+"/crab_giant_pulses1_2020-03-17T19:25:13,_17901936.rawudp", "rb") as f:
        map1 = np.memmap(f, mode="r", dtype=np.int8)
        x_imag=np.array(map1[i*N:(i+1)*N]).astype(np.int8)
        del map1
    f.close
    with open(path+"/crab_giant_pulses2_2020-03-17T19:25:13,_17901936.rawudp", "rb") as f:
        map2 = np.memmap(f, mode="r", dtype=np.int8)
        y_real=np.array(map2[i*N:(i+1)*N]).astype(np.int8)
        del map2
    f.close()
    with open(path+"/crab_giant_pulses3_2020-03-17T19:25:13,_17901936.rawudp", "rb") as f:
        map3 = np.memmap(f, mode="r", dtype=np.int8)
        y_imag=np.array(map3[i*N:(i+1)*N]).astype(np.int8)
        del map3
    f.close()
    x_real=x_real.flatten()
    x_imag=x_imag.flatten()
    y_real=y_real.flatten()
    y_imag=y_imag.flatten()
    stokesQ=np.empty_like(x_real, dtype=np.int32) 
    chunks=13
    chunksize=int(x_real.shape[0]/chunks)
    for j in range(chunks):
        stokesQ[j*chunksize:(j+1)*chunksize] =(
        np.square(x_real[j * chunksize: (j+1) * chunksize].astype(np.int32)) +
        np.square(x_imag[j * chunksize: (j+1) * chunksize].astype(np.int32)) -
        np.square(y_real[j * chunksize: (j+1) * chunksize].astype(np.int32)) -
        np.square(y_imag[j * chunksize: (j+1) * chunksize].astype(np.int32)))
    output=open('/mnt/ucc2_data1/data/giesec/crab/raw_filterbank_files/1936_Q.fil', 'ab')
    output.write(stokesQ)
    output.close()


