#!/bin/bash

if [ -z $1 ]
then

	echo "This script needs 1 argument, a list with IPs to check"
	exit 1

fi

echo "" >  output

while read p
do

	echo "Checking the ip: $p"

	shodan host $p > ouptut 2>/dev/null

done < $1
