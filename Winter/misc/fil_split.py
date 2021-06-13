from blimpy import Waterfall
import numpy as np
import matplotlib.pyplot as plt
import math as m
import os
import argparse
from turbo_seti.find_event.find_event import read_dat

parser = argparse.ArgumentParser(description='Plot all hits in a .dat file for further inspection')

parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
parser.add_argument("-i", "--inputfile", help="Name of .fil/.dat file")
#parser.add_argument("-fl", "--lower_fbound", help="lower bound of frequency range")
#parser.add_argument("-fu", "--upper_fbound", help="upper bound of frequency range")


args = parser.parse_args()
inputfile=args.inputfile

fil_file=inputfile+'.fil'
dat_file=inputfile+'.dat'

df=read_dat(dat_file)
low_freqs=df['FreqStart']
high_freqs=df['FreqEnd']
snr=df['SNR']
drift_rates=df['DriftRate']

for i in range(len(low_freqs)):
	f0=low_freqs[i]
	f1=high_freqs[i]

	data=Waterfall(fil_file,
				   f_start=f0,
				   f_stop=f1)

	fig=plt.figure(1)
	ax=fig.add_subplot(111)
	waterfall=ax.imshow(data, cmap='viridis')
	plt.savefig()
