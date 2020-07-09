import numpy as np 
import matplotlib.pyplot as plt 
import csv
import pandas as pd 
import sys


SNs=['1','3','5','7','9']
times=['2', '4', '6', '8', '0']
names=['1','2','3','4','5','6','7','8','9','0']
data=pd.read_csv(sys.argv[1], sep='\s+', 
names=names)

SN=[]
for i in SNs :
    col=data[i].values
    for j in col:
        SN.append(j)

SN_arr=np.array(SN)

time=[]
for i in times:
    col=data[i].values
    for j in col:
        time.append(j)
    
time_arr=np.array(time)

pd.DataFrame(time_arr, SN_arr).to_csv(
sys.argv[2])#,
# header=None, index=None)


#print(sys.argv[1])
#print(sys.argv[2])


