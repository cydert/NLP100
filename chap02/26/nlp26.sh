#!/bin/bash

n=$1
size=$( cat ../popular-names.txt | wc -l )
one_size=$(( size / n ))
remain=$(( size % n ))
if [ $remain -gt 0 ]; then
	one_size=$(( one_size + 1 ))
fi
split -l $one_size ../popular-names.txt 

