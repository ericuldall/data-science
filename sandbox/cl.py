#!/usr/bin/python
import sys

args = sys.argv

if args[1] == '-a':
	total = 0
	for num in args[2:]:
		total += int(num)


if args[1] == '-m':
	total = 1;
	for num in args[2:]:
		total *= int(num)

print( total )
