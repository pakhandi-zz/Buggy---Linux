for i in 0 1 2 3 4 5 6 7 8 9 10 11 12
do
	FILE=in$i.txt
	OUTFILE=out$i.txt
	if [ -f $FILE ]; then
		#echo "exists"
		echo "Running Test Case " $i
		echo "\n"
		echo "Input : "
		cat $FILE
		echo "\n"
		./$1 < in$i.txt > o.txt
		echo "Your Output : "
		cat o.txt
		echo "\n"
		echo "Correct Output : "
		cat $OUTFILE
		echo "\n"
		echo "----------------------------------------"
	fi
done