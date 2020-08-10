import matplotlib.pyplot as plt
from blimpy import Waterfall
from turbo_seti.find_doppler.find_doppler import FindDoppler
import turbo_seti.find_event as find
import numpy as np
import pandas as pd
from turbo_seti import plot_event
from turbo_seti.find_event.find_event import make_table
import os

path='/home/charlesg/turboSETI/oumuamua_files/'
png_path='/home/charlesg/turboSETI/blc00_Graphs/oumuamua/'

filenames=['OUMUAMUA_0011.gpuspec.0002',
           'OUMUAMUA_OFF_0012.gpuspec.0002',
           'OUMUAMUA_0013.gpuspec.0002',
           'OUMUAMUA_OFF_0014.gpuspec.0002',
           'OUMUAMUA_0015.gpuspec.0002',
           'OUMUAMUA_OFF_0016.gpuspec.0002']

exts=['.dat', '.log']

max_drift_rate = 4 #Hz/s
SNR = 10

for file_name in filenames:
    dat_file=path+file_name+'.dat'
    fil_file=path+'fil_files/'+file_name+'.fil'

    print('Deleting previous results')
    for ext in exts:
        if os.path.exists(path+file_name+ext):
            os.remove(path+file_name+ext)
        else:
            continue

    print('Searching'+fil_file)
    find_signal=FindDoppler(fil_file, max_drift=max_drift_rate, snr=SNR,
                            out_dir=path)
    find_signal.search()

    print('Generating Dataframe')
    df = make_table(dat_file)
    df = df.set_index('TopHitNum')
    df.sort_values('SNR')
    print(df)
    hits=df.index.values.tolist()

    print('Top Hits are: ', hits)

    fig=plt.figure(figsize=(12, 8))
    if len(hits) <= 5: 
        for i in range(len(hits)): 
            plt.subplot(len(hits)//2 +1, 2, i+1) 
            plot_event.plot_hit(fil_filename =fil_file, dat_filename = dat_file,
                                hit_id = i, offset=20)
    else:
        for i in range(6):
            plt.subplot(3, 2, i+1)
            plot_event.plot_hit(fil_filename =fil_file, dat_filename = dat_file,
                                hit_id = i, offset=40)

    fig.tight_layout()
    plt.savefig(png_path+file_name+'_SNR'+str(SNR)
    +'_Dmax'+str(max_drift_rate)+'.png')

