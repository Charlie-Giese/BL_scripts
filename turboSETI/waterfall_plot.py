import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from turbo_seti import plot_event
from blimpy import Waterfall
import os


path='/home/charlesg/turboSETI/oumuamua_files/fil_files/'
png_path='/home/charlesg/turboSETI/blc00_Graphs/oumuamua/'

filenames=[path+'OUMUAMUA_0011.gpuspec.0002.fil',
           path+'OUMUAMUA_OFF_0012.gpuspec.0002.fil',
           path+'OUMUAMUA_0013.gpuspec.0002.fil',
           path+'OUMUAMUA_OFF_0014.gpuspec.0002.fil',
           path+'OUMUAMUA_0015.gpuspec.0002.fil',
           path+'OUMUAMUA_OFF_0016.gpuspec.0002.fil']


fig=plt.figure(figsize=(12,8))

plot_event.make_waterfall_plots(filenames, target='Oumuamua', drates, fvals, 
                                f_start=3076.8, f_stop=3078.2, 
                                node_string=None, filter_level=None, ion=False, epoch=None, 
                                bw=250.0, local_host='', plot_name=png_path+'test',
                                save_pdf_plot=True, 
                                saving_fig=True, offset=50, dedoppler=False)

plt.savefig(png_path+'test.py')
