#! bin/bash

for c in 1 2 3 4 5 6 7 8 9 A B C D;
do
	
	cat "SMC021_008"$c"1.pls" >> SMC021_008.temp.pls
		
	
	sort -g SMC021_008.temp.pls | uniq >> SMC021_008.pls
	rm SMC021_008.temp.pls
done
