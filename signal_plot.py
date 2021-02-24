
from blimpy import Waterfall
from blimpy import dice
import numpy as np
import matplotlib.pyplot as plt
import math as m
import os
import argparse
from turbo_seti.find_event.find_event import read_dat
from turbo_seti.find_event.plot_event import plot_waterfall
from turbo_seti import plot_event
from astropy.time import Time
import matplotlib
from blimpy.utils import rebin
import sys

#fontsize=26
#font = {'family' : 'DejaVu Sans',
#'size' : fontsize}
MAX_IMSHOW_POINTS = (4096, 1268)

def overlay_drift(f_event, f_start, f_stop, drift_rate, t_duration, offset=0):
    r'''
    Creates a dashed red line at the recorded frequency and drift rate of
    the plotted event - can overlay the signal exactly or be offset by
    some amount (offset can be 0 or 'auto').
    '''
    # determines automatic offset and plots offset lines
    if offset == 'auto':
        offset = ((f_start - f_stop) / 10)
        plt.plot((f_event - offset, f_event),
                 (10, 10),
                 "o-",
                 c='#cc0000',
                 lw=2)

    # plots drift overlay line, with offset if desired
    plt.plot((f_event + offset, f_event + drift_rate/1e6 * t_duration + offset),
             (0, t_duration),
             c='#cc0000',
             ls='dashed', lw=2)

filename=sys.argv[1]+'.h5'
dat_file=sys.argv[1]+'.dat'
on_source_name='TESS_TOI_1449'

df=read_dat(dat_file)
low_freqs=106.5962
high_freqs=106.5962
snr=df['SNR']
drift_rates=df['DriftRate']

#matplotlib.rc('font', **font)

#for i in range(len(low_freqs)):
f0=low_freqs
f1=high_freqs
f_mid = round(np.abs(f0+f1)/2., 4)
mid_f = round(np.abs(f0+f1)/2., 4)

f_start=mid_f-8e-4
f_stop=mid_f+8e-4

plt.figure(1)# figsize=(14,10))
fil = Waterfall(filename, f_start=f_start, f_stop=f_stop)#, t_start=40, t_stop=60)

dummy, plot_data = fil.grab_data()

# rebin data to plot correctly with fewer points
dec_fac_x, dec_fac_y = 1, 1
if plot_data.shape[0] > MAX_IMSHOW_POINTS[0]:
	dec_fac_x = plot_data.shape[0] / MAX_IMSHOW_POINTS[0]
if plot_data.shape[1] > MAX_IMSHOW_POINTS[1]:
	dec_fac_y =  int(np.ceil(plot_data.shape[1] /  MAX_IMSHOW_POINTS[1]))
plot_data = rebin(plot_data, dec_fac_x, dec_fac_y)




	# read in data
fig=plt.figure(1)
t0 = fil.header['tstart']
	# make plot with plot_waterfall
source_name = 'B1919+54'
this_plot = fil.plot_waterfall(f_start=f_start, f_stop=f_stop)
plt.suptitle("")
plt.title("")
# calculate parameters for estimated drift line
#t_elapsed = Time(fil.header['tstart'], format='mjd').unix - Time(t0, format='mjd').unix
#t_duration = (fil.n_ints_in_file - 1) * fil.header['tsamp']
#f_event = f_mid + drift_rate / 1e6 * t_elapsed
#offset=0
# plot estimated drift line
#overlay_drift(f_event, f_start, f_stop, drift_rate, t_duration, offset)

	# Title the full plot

#plot_title = "%s \n  MJD:%5.5f" % (source_name, t0)

#plt.title(plot_title)
	# Format full plot
plt.xticks(np.linspace(f_start, f_stop, num=4), ['','','',''])

	# More overall plot formatting, axis labelling
factor = 1e6
units = 'Hz'

ax = plt.gca()
plt.tight_layout()
xloc = np.linspace(f_start, f_stop, 5)
xticks = [round(loc_freq) for loc_freq in (xloc - mid_f)*factor]
if np.max(xticks) > 1000:
	xticks = [xt/1000 for xt in xticks]
	units = 'kHz'
plt.xticks(xloc, xticks)
plt.xlabel("Relative Frequency [%s] from %f MHz"%(units,mid_f))
	
	
plt.savefig('B1919+54.png')
plt.close('all')




