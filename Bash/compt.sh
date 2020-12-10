#!/bin/bash
let "a = 0"

while [ $a -ne 6 ]
do 
	echo $a
	a=$(($a+1))
done

