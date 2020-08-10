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

name=4

dat_file=path+filenames[name]+'.dat'
fil_file=path+'fil_files/'+filenames[name]+'.fil'

df = make_table(dat_file)
df = df.set_index('TopHitNum')
df.sort_values('SNR')

i=4

fig=plt.figure()
plot_event.plot_hit(fil_filename =fil_file, dat_filename = dat_file,
                    hit_id = i, offset=50)

plt.savefig(png_path+filenames[name]+'_hit_'+str(i)+'_.png')
