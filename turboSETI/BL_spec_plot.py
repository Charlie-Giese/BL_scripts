import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from blimpy import Waterfall


path='/home/charlesg/turboSETI/trappist1/'
fil_path=path+'fil_files/high/'
png_path='/home/charlesg/turboSETI/blc00_Graphs/trappist1/hits'
dat_path=path+'doppler_output/'


filenames=['blc00_guppi_57807_75725_DIAG_TRAPPIST1_0015.gpuspec.0000',
           'blc00_guppi_57807_75805_DIAG_TRAPPIST1_OFF_0016.gpuspec.0000',
           'blc00_guppi_57807_75885_DIAG_TRAPPIST1_0017.gpuspec.0000',
           'blc00_guppi_57807_75965_DIAG_TRAPPIST1_OFF_0018.gpuspec.0000']

f_start=2177.969679
f_stops=2177.969929


obs=Waterfall(path+'fil_files/high/'+filenames[2]+'.fil')
obs.plot_spectrum(logged=True, f_start=f_start, f_stop=f_stops)
plt.savefig(path+'trappis1_spectra.png')


#
