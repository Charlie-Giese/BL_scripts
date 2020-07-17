import numpy as np
import matplotlib.pyplot as ply
import os
import sys
from  sigpyproc.Readers import FilReader

file=FilReader("1936I_rmrfit.fil")

file.downsample(tfactor=32, ffactor=1, filename="1936I_rmrfit_readyforDD.fil")
downsampled_file=FilReader("1936I_rmrfit_readyforDD.fil")

#channel98=downsampled_file.getChan(198)
#channel98.toFile("channel198.tim")

timeseries=downsampled_file.dedisperse(57)
timeseries.toFile("1936I_rmrfit_DD.tim")

downsampled_tseries=timeseries.downsample(32)
downsampled_tseries.tofile("1936I_rmrfit_D32.tim")

#bandpass=downsampled_file.bandpass()
#bandpass.toFile("1936I_rmrfit_bandpass.tim")

#collapse=downsampled_file.collapse()
#collapse.toFile("0DM_timeseries.tim")
