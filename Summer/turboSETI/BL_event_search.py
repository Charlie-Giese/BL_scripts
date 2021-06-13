import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from turbo_seti.find_event.find_event_pipeline import find_event_pipeline
from turbo_seti.find_event.plot_event_pipeline import plot_event_pipeline



path='/home/charlesg/turboSETI/trappist1/'
fil_path=path+'fil_files/high'
png_path='/home/charlesg/turboSETI/blc00_Graphs/trappist1/hits'
dat_path=path+'doppler_output/'


dat_list=[dat_path+'blc00_guppi_57807_75725_DIAG_TRAPPIST1_0015.gpuspec.0000.dat',
          dat_path+'blc00_guppi_57807_75805_DIAG_TRAPPIST1_OFF_0016.gpuspec.0000.dat',
          dat_path+'blc00_guppi_57807_75885_DIAG_TRAPPIST1_0017.gpuspec.0000.dat',
          dat_path+'blc00_guppi_57807_75965_DIAG_TRAPPIST1_OFF_0018.gpuspec.0000.dat']


check_zero_drift = False
filter_threshold = 3
number_in_cadence=4

with open(dat_path+'dat_files.lst', 'w') as f:
    for item in dat_list:
        f.write("%s\n" % item)

event_dataframe = find_event_pipeline(dat_path+'dat_files.lst', 
                                      number_in_cadence=number_in_cadence,  
                                      filter_threshold=filter_threshold)

print(event_dataframe)




#
