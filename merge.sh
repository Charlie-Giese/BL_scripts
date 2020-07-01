#! bin/bash

for c in 1 2 3 4 5 6 7 8 9 A B C D;
do
	cd "/mnt/ucc2_data1/data/giesec/SMC/archive"/$c

	for i in {0..500};
	do

		cat  "SMC021_008"$c"1."$i".pls" >> ./"SMC021_008"$c"1.temp.pls"
	done
	sort -g "SMC021_008"$c"1.temp.pls" | uniq >> "SMC021_008"$c"1.pls"
	mv "SMC021_008"$c"1.pls" /mnt/ucc2_data1/data/giesec/SMC/archive/Files
done
