#!/usr/bin/python2.7
import sys

lc = 0
wc = 0

for line in sys.stdin:
	line = line.strip()
	print 'line\t', 1
	for word in line.split():
		print 'word\t', 1
