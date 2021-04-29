#!/bin/bash

if [ -z "$1" ] | [ -z "$2" ] | [ "$1" == "-h" ]
then

	echo -e "This bash script needs two input args to work\n"
	echo -e "./webChecker.sh [-h] <arg1> <arg2> [-v]\n"
	echo -e "\targ1: Input file with IPs to check the availability of these"
	echo -e "\targ2: Output file"
	echo -e "\t-h: Display this help and exit"
	echo -e "\t-v, -vv: Verbose mode and extra verbosity"
	exit 1

fi

if [ -n "$3" ]
then

	if [ "$3" == "-v" ]
	then

		verb="1"

	elif [ "$3" == "-vv" ]
	then

		verb="2"

	else

		echo -e "Optional flag can only be '-v'"
		exit 1

	fi

else

	verb="0"

fi


echo "" > $2

while IFS= read -r line
do

	echo "" > tmp

	if [ $verb == 1 ]
	then

		echo "Checking for http://$line ..."
		curl -Is $line | head -n 1 > tmp & sleep 4; kill $! &>/dev/null

	elif [ $verb == 2 ]
	then

		echo "Checking for http://$line ..."
		echo -e "IP: $line \n" >> $2
		curl -Is $line | head -n 1 | tee tmp & sleep 4; kill $! &>/dev/null

	else

		curl -Is $line | head -n 1 > tmp & sleep 4; kill $! &>/dev/null

	fi

	if [ -s tmp ]
	then

		echo "IP: $line -" $(cat tmp) >> $2
	#if tmp tiene algo lo guardo si no guardo no hay output

	else

		echo "IP: $line - Dont respond" >> $2

	fi

	sleep 1


done < "$1"

exit 0
