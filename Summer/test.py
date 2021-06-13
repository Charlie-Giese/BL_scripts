from blimpy import Waterfall
from blimpy import dice
import numpy as np
import matplotlib.pyplot as plt
import math as m
import os
import argparse
from turbo_seti.find_event.find_event import read_dat
from turbo_seti import plot_event


fil_file='guppi_58306_48602_125402_G47.48+1.41_0001.0002.fil'



obs=Waterfall(fil_file)

fig=plt.figure(1)
obs.plot_waterfall()
plt.show()
