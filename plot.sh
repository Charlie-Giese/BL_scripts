#! bin/bash


path="/mnt/ucc2_data1/data/giesec/SMC/archive"	

for file in 1 2 3 4 5 6 7 8 9 A B C D
do
	rm $path/$file/plot.py
	cp -f $path/plot.py  $path/$file
	cd $path/$file/
	python3 plot.py "SMC021_008"$file"1.fil"
	mv -f pic.png $file".png"
	mv -f  $file".png" /mnt/ucc2_data1/data/giesec/SMC/images
done
