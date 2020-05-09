#!/bin/bash

sort ../popular-names.txt -r -t $'\t' -k 3 -n
