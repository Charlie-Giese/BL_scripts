import numpy as np
import matplotlib.pyplot as plt


stokesI=np.load("1936I.npy")

mean_list=[]
chan_list=[]
for i in range(488):
    chan=stokesI[:, i]
    temp=np.mean(chan, axis=0)
    mean_list.append(temp)
    chan_list.append(i)
means=np.array(mean_list)
channels=np.array(chan_list)
indices=np.argwhere(means >= 800)
outliers=channels[indices]


