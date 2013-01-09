#!/bin/bash

if [ "x$1" = "x" ]; then
	echo "Usage: $0 <PROBLEM_NUMBER>"
	exit 1
fi

mkdir $1
cp ./skeleton.py $1/problem$1.py

echo "Created dir $1. Copied skeleton.py to $1/problem$1.py."