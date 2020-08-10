import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from turbo_seti import plot_event
from turbo_seti.find_event.find_event import make_table
import os
from turbo_seti.find_event.find_event_pipeline import find_event_pipeline
import blimpy
import turbo_seti
import turbo_seti.find_doppler.seti_event as turbo
import turbo_seti.find_event as find


path='/home/charlesg/turboSETI/oumuamua_files/'
png_path='/home/charlesg/turboSETI/'

fil_files=[path+'fil_files'+'OUMUAMUA_0011.gpuspec.0002.fil',
           path+'fil_files'+'OUMUAMUA_OFF_0012.gpuspec.0002.fil',
           path+'fil_files'+'OUMUAMUA_0013.gpuspec.0002.fil',
           path+'fil_files'+'OUMUAMUA_OFF_0014.gpuspec.0002.fil',
           path+'fil_files'+'OUMUAMUA_0015.gpuspec.0002.fil',
           path+'fil_files'+'OUMUAMUA_OFF_0016.gpuspec.0002.fil']

dat_files=[path+'OUMUAMUA_0011.gpuspec.0002.dat',
           path+'OUMUAMUA_OFF_0012.gpuspec.0002.dat',
           path+'OUMUAMUA_0013.gpuspec.0002.dat',
           path+'OUMUAMUA_OFF_0014.gpuspec.0002.dat',
           path+'OUMUAMUA_0015.gpuspec.0002.dat',
           path+'OUMUAMUA_OFF_0016.gpuspec.0002.dat']


check_zero_drift = True
filter_threshold = 1
SNR_cut = 5


event_dataframe = find.find_events(dat_files, 
                                   SNR_cut=SNR_cut, 
                                   check_zero_drift=check_zero_drift, 
                                   filter_threshold=filter_threshold, 
                                   on_off_first='ON')

event_csv_string='OUMUAMUA_events__f'+str(filter_threshold)+'_SNR'+str(SNR_cut)+'.csv'

print(event_dataframe)
event_dataframe.to_csv(path+event_csv_string)
fils_list_string = "fil_files.lst" #just a file containing the .fil names
turbo_seti.plot_event_pipeline.plot_event_pipeline(event_csv_string, 
                                                   fil_files,  
                                                   user_validation=False,
                                                   offset=0,
                                                   plot_snr=False)





#
