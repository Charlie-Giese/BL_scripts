import matplotlib.pyplot as plt
from blimpy import Waterfall
from turbo_seti.find_doppler.find_doppler import FindDoppler
import turbo_seti.find_event as find
import numpy as np
import pandas as pd
from turbo_seti import plot_event
from turbo_seti.find_event.find_event import make_table
import os

path='/home/charlesg/turboSETI/psr_files'
png_path='/home/charlesg/turboSETI/'

filenames=['/DIAG_PSR_J0953+0755_0003.gpuspec.0002',
           '/DIAG_PSR_J0953+0755_0003.gpuspec.0001',
           '/DIAG_PSR_J0953+0755_0003.gpuspec.0000']

exts=['.dat', '.log', '.h5']

max_drift_rate = 1 #Hz/s
signal_to_noise = 25

for file_name in filenames:
    for ext in exts:
        if os.path.exists(path+file_name+ext):
            os.remove(path+file_name+ext)
        else:
            continue
    find_signal=FindDoppler(path+file_name+'.fil', max_drift=max_drift_rate, snr=signal_to_noise,
                            out_dir=path)
    fil_file=path+file_name+'.fil'
    dat_file=path+file_name+'.dat'
    find_signal.search()
    df = make_table(dat_file)
    df = df.set_index('TopHitNum')
    df = df.sort_values('SNR')
    print(df)
    hits=df.index.values.tolist()
    print(len(hits), hits)
    fig=plt.figure()
    if len(hits) <= 5: 
        for i in range(len(hits)): 
            print(i, hits[i])
            plt.subplot(len(hits), 1, i+1) 
            plot_event.plot_hit(fil_filename =fil_file, dat_filename = dat_file,
                                hit_id = i)
    else:
        for i in range(4):
            plt.subplot(5, 1, i+1)
            plot_event.plot_hit(fil_filename =fil_file, dat_filename = dat_file,
                                hit_id = i)
    plt.savefig(png_path+file_name+'.png')

