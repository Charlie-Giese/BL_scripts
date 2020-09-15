import matplotlib.pyplot as plt
from blimpy import Waterfall
from turbo_seti.find_doppler.find_doppler import FindDoppler
import numpy as np
import pandas as pd
from turbo_seti.find_event.find_event import make_table
import os
from turbo_seti.find_event.find_event_pipeline import find_event_pipeline


path='/home/charlesg/turboSETI/trappist1/'
fil_path=path+'fil_files/high/'
png_path='/home/charlesg/turboSETI/blc00_Graphs/trappist1/hits'
dat_path=path+'doppler_output/'


filenames=['blc00_guppi_57807_75725_DIAG_TRAPPIST1_0015.gpuspec.0000',
           'blc00_guppi_57807_75805_DIAG_TRAPPIST1_OFF_0016.gpuspec.0000',
           'blc00_guppi_57807_75885_DIAG_TRAPPIST1_0017.gpuspec.0000',
           'blc00_guppi_57807_75965_DIAG_TRAPPIST1_OFF_0018.gpuspec.0000']

max_drift_rate = 1 #Hz/s
SNR = 25

for file_name in filenames:
    dat_file=dat_path+file_name+'.dat'
    fil_file=fil_path+file_name+'.fil'

    #if os.path.exists(dat_file):
    #    continue
    #else:
        #print('Searching'+fil_file)
    find_signal=FindDoppler(fil_file, max_drift=max_drift_rate, snr=SNR,
                        out_dir=dat_path)
    find_signal.search()

    print('Generating Dataframe')
    df = make_table(dat_file)
    df_sorted = df.set_index('TopHitNum')
    df.sort_values('SNR')
    print(df)
    hits=df.index.values.tolist()

    print('Top Hits are: ', hits)


