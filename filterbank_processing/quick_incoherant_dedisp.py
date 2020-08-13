import argparse
import os
import numpy as np
import matplotlib.pyplot as plt
import datetime

nchan = 488
sampleRate = 5.12 * 10** -6
# Top of sb499
ftop = 197.4609375
dm=61.252
foff=-0.1953125

def dm_delays(ftop, foff, nchan, dm):
	# Implements the standard DM delay
	freqs = ftop + 0.5 * foff + foff * np.arange(nchan)
	delays = np.hstack([[0.], 4150 * dm * ((1. / np.square(freqs[1:])) - (1. / np.square(freqs[0])))])

	return delays


def main(s0, s1, s2, s3, delayFunc, dm, decimate = 0):

	# Get the delays (in seconds)
	print("Finding time delays...")
	delays = delayFunc(absftop, -100. / 512, nchans, dm)
	print("Delays (s):")
	print(delays)
	delays /= sampleRate
	delays = delays.astype(int)

	# Build up a 
	outputLen = int(s0.shape[0] - np.max(delays))
	dataOut = np.ones((outputLen, nchans), dtype = np.int32)
	print(delays)

	# Terribl approach to RFI
	#zapchans = list(range(150,200)) + list(range(280, 290)) + list(range(305, 320)) + list(range(450, nchans))

	# SImple implementation that works, but isn't cache efficient
	print("Forming Stokes I + Dedispersing... processing channel:")
	for i in range(nchans):
		#if i in zapchans:
			#continue
		#print(f"{i} ({100 * i / min(430,nchans)} %)", end = '\r')
		dataOut[..., i] += np.square(s0[delays[i]: delays[i] + outputLen, i].astype(np.int32))
		dataOut[..., i] += np.square(s1[delays[i]: delays[i] + outputLen, i].astype(np.int32))
		dataOut[..., i] += np.square(s2[delays[i]: delays[i] + outputLen, i].astype(np.int32))
		dataOut[..., i] += np.square(s3[delays[i]: delays[i] + outputLen, i].astype(np.int32))


	if decimate:
		print("Decimating...")
		rollingSum = np.cumsum(dataOut, axis = 0)
		dataOut = rollingSum[decimate::decimate, :] - rollingSum[:-decimate:decimate, :]


	print("Plotting...")
	plt.figure(figsize = (24,12))
	plt.imshow(dataOut.T, aspect = 'auto', vmax = np.percentile(dataOut, 95), vmin = np.percentile(dataOut, 33))
	#plt.savefig(f'./debugfull_{datetime.datetime.now().isoformat()}.png')
	plt.savefig('test1.png')
	plt.figure(figsize = (24,12))
	plt.imshow(np.log10(dataOut.T), aspect = 'auto', vmax = np.log10(np.percentile(dataOut, 95)), vmin = np.log10(np.percentile(dataOut, 33)))
	#plt.savefig(f'./debugfull2_{datetime.datetime.now().isoformat()}.png')
	plt.savefig('test2.png')
	plt.figure(figsize = (24,12))
	d1 = dataOut[:, :100].sum(axis = 1)
	d1 -= np.mean(d1, dtype = np.int64)
	d2 = dataOut[:, 100:200].sum(axis = 1)
	d2 -= np.mean(d2, dtype = np.int64)
	d3 = dataOut[:, 200:300].sum(axis = 1)
	d3 -= np.mean(d3, dtype = np.int64)
	d4 = dataOut[:, 300:].sum(axis = 1)
	d4 -= np.mean(d4, dtype = np.int64)
	plt.plot(d1, alpha = 0.3, label = '1')
	plt.plot(d2, alpha = 0.3, label = '2')
	plt.plot(d3, alpha = 0.3, label = '3')
	plt.plot(d4, alpha = 0.3, label = '4')
	plt.legend()
	#plt.savefig(f'./debug_{datetime.datetime.now().isoformat()}.png')
	plt.savefig('test3.png')
	print("Done!")

# Load in the data

path='/mnt/ucc2_data1/data/giesec/J0218+4232/20200626040200J0218+4232/rawudp/'

s0=open(path+"16310_.rawudp", "rb")
s1=open(path+"16310_.rawudp", "rb")
s2=open(path+"16310_.rawudp", "rb")
s3=open(path+"16310_.rawudp", "rb")

s0 = np.fromfile(path+'16130_.rawudp', dtype = np.int8).reshape(-1, nchans)
s1 = np.fromfile(path+'16131_.rawudp', dtype = np.int8).reshape(-1, nchans)
s2 = np.fromfile(path+'16132_.rawudp', dtype = np.int8).reshape(-1, nchans)
s3 = np.fromfile(path+'16133_.rawudp', dtype = np.int8).reshape(-1, nchans)

main(s0, s1, s2, s3, delayFunc, dm, decimate = 0)



<<<<<<< HEAD
=======
	print("Starting dedispersion...")
	main(s0, s1, s2, s3, args.delayFunc, args.dm, args.decimate)
>>>>>>> 79e1de97d91c5962f412478307510f1405af3e99
