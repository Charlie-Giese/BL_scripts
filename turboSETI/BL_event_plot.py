import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import glob
from turbo_seti.find_event.plot_event_pipeline import plot_event_pipeline

path='/home/charlesg/turboSETI/trappist1/fil_files/high/'


filelist = glob.glob(path+'*.fil')

with open('fil_files.lst', 'w') as f:
    for item in filelist:
        f.write("%s\n" % item)

threshold=3
snr=10
target='TRAPPIST1'

csv_path='/home/charlesg/turboSETI/trappist1/'
csv_string='DIAG_'+target+'_f'+str(threshold)+'_snr'+str(snr)+'.csv'

plot_event_pipeline(csv_string,
                    'fil_files.lst',
                    user_validation=True)
