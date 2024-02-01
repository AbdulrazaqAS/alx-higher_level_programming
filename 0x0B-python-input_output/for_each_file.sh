#!/bin/bash

# Usage:
# ./for_each_file.sh "*.py" echo '#!/usr/bin/python3'

for f in $1 ;
do
	echo $f
	if [ "$2" == "echo" ]
	then
		if [ "$#" == 3 ]
		then
			echo hi
			"$2" "$3" >> $f
		fi
	else
		"$2" $f
	fi
done
