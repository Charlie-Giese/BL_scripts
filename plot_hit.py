from os.path import dirname
import sys
import matplotlib
matplotlib.use('agg')

#General packages import
import numpy as np
import logging; logging.disable(logging.CRITICAL)
from astropy.time import Time

#BL imports
import blimpy as bl
from blimpy.utils import rebin

#Plotting packages import
import matplotlib.pyplot as plt

#preliminary plot arguments
#fontsize=16
#font = {'family' : 'DejaVu Sans',
#'size' : fontsize}
MAX_IMSHOW_POINTS = (4096, 1268)
import os

def plot_waterfall(fil,
                   source_name,
                   f_start=None,
                   f_stop=None,
                   f_scrunch=1,
                   **kwargs):

    """ Plot waterfall of data in a .fil or .h5 file
    Args:
        fil (str): filterbank file containing the dynamic spectrum data
        source_name (str): name of the target
        f_start (float): start frequency, in MHz
        f_stop (float): stop frequency, in MHz
        f_scrunch (int): Average across frequency channels
        kwargs: keyword args to be passed to matplotlib imshow()
    """
    file1=os.getcwd()+'/'+fil
    #prepare font
    #matplotlib.rc('font', **font)
    fil = bl.Waterfall(file1, f_start=f_start, f_stop=f_stop)
    #Load in the data from fil
    plot_f, plot_data = fil.grab_data(f_start=f_start, f_stop=f_stop)

    #Make sure waterfall plot is under 4k*4k
    dec_fac_x, dec_fac_y = 1, 1

    if dec_fac_y == 1 and f_scrunch > 1:
        dec_fac_y = f_scrunch

    #rebinning data to plot correctly with fewer points
    if plot_data.shape[0] > MAX_IMSHOW_POINTS[0]:
        dec_fac_x = plot_data.shape[0] / MAX_IMSHOW_POINTS[0]
    if plot_data.shape[1] > MAX_IMSHOW_POINTS[1]:
        dec_fac_y =  int(np.ceil(plot_data.shape[1] /  MAX_IMSHOW_POINTS[1]))
    plot_data = rebin(plot_data, dec_fac_x, dec_fac_y)

    #fix case where frequencies are reversed by fil.grab_data() # Shane Smith PR #82
    if plot_f[-1] < plot_f[0]:
        plot_f = plot_f[::-1]
        plot_data = plot_data[:, ::-1]

    #determine extent of the plotting panel for imshow
    extent=(plot_f[0], plot_f[-1], (fil.timestamps[-1]-fil.timestamps[0])*24.*60.*60, 0.0)

    #plot and scale intensity (log vs. linear)
    kwargs['cmap'] = kwargs.get('cmap', 'viridis')
    kwargs['logged'] = True
    if kwargs['logged'] == True:
        plot_data = 10*np.log10(plot_data)
        kwargs.pop('logged')



    #get normalization parameters
    vmin = plot_data.min()
    vmax = plot_data.max()
    normalized_plot_data = (plot_data - vmin) / (vmax - vmin)



    #display the waterfall plot
    this_plot = plt.imshow(normalized_plot_data,
        aspect='auto',
        rasterized=True,
        interpolation='nearest',
        extent=extent,
        **kwargs
    )

    #add plot labels
    plt.xlabel("Frequency [Hz]",fontdict=font)
    plt.ylabel("Time [s]",fontdict=font)

    #add source name
    ax = plt.gca()
    #plt.text(0.03, 0.8, source_name, transform=ax.transAxes, bbox=dict(facecolor='white'))
    #if plot_snr != False:
    #    plt.text(0.03, 0.6, plot_snr, transform=ax.transAxes, bbox=dict(facecolor='white'))
    #return plot
    return this_plot


fil=sys.argv[1]
source_name = sys.argv[2]
f_start=sys.argv[3]
f_stop=sys.argv[4]

plot_waterfall(fil, source_name, f_start=None, f_stop=None, f_scrunch=1)
