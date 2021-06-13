#!/bin/bash
export _POSIX2_VERSION=199209


#20180921.fil
#Looping through each filterbank file



for DM in $(seq 0 0.003 30);
do
#looping through each DM trial for each fil file
        
        
    echo "Dedispersing at" $DM "pc/cc"    
    dedisperse 20180921.fil -d $DM > "20180921."$DM".tim" #dedispersing
    seek "20180921."$DM".tim" -pulse -fftw #-s does fftw  
    #outputs .pls .prd .top .tim .spc .hst
    rm -r *.top
    rm -r *.hst
    rm -r *.tim
    #rm -r *.spc

done
mv *.prd archive/prd/
mv *.pls archive/pls/


