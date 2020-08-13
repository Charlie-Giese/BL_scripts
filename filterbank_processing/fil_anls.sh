#! bin/bash

"""
This script creates a psd plot of a time interval of a filterbank file. It first increases the dynamic range, then cuts a a chunk of time of length $width around a timesample $tim. awk command at the bottom of the file is an example of how to find the correct timestamp of a pulse. 
"""

file=$1
tim=$2
width=$3
name=$4
sigproc=/home/obs/Evan/sigproc/src


$sigproc/decimate $file -t 8 -c 1 -n 8 > lb.fil
$sigproc/chop_fil lb.fil -s $tim -r $width > lb.chop.fil
$sigproc/reader lb.chop.fil > lb.ascii 
awk '{for (i=0;i<96;i++) printf "%f %d %f\n",$1,i,$i}' lb.ascii >  $name".ascii"
python3 raw8bitplot.py $name".ascii" $name
rm lb.fil
rm lb.chop.fil
rm lb.ascii
rm $name".ascii"

"""
awk NR!=1{if ($1>200 && $1<500 && $3<8000000) print $0} $1  | sort -gr -k4 | head -60| awk '{print $1,$4}' >
this command outputs the top 60 S/N before 8000s between 200 and 500 DM
this can be dumped to text file for plotting, allows an estimate of DM.
can also do this for width instead of DM; S/N peaks around DM/width estimate
"""
