#! bin/bash

cd archive/pls/

for DM in $(seq 0 0.0015 15);
do 

	cat "20180921."$DM".pls" >> "20180921.temp.pls"
done

sort -g 20180921.temp.pls | uniq >> 20180921.pls


for DM in $(seq 15 0.0030 30);
do

        cat "20180921."$DM".pls" >> "20180921.temp.pls"
done

sort -g 20180921.temp.pls | uniq >> 20180921.pls


 
