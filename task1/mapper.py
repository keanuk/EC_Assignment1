#!/usr/bin/python2.7
import sys

for line in sys.stdin:
	line = line.strip()
	words = line.split()
	print 'line'
	for word in words:
		print 'word'
