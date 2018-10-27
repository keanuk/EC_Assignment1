#!/usr/bin/env python2
import sys

count = 0
prevGenre = None

for line in sys.stdin:
    genre, c = line.strip().split('\t')
    if genre == prevGenre:
        count += int(c)
    elif prevGenre == None:
        prevGenre = genre
        count += int(c)
    else:
        print prevGenre, '\t', count
        prevGenre = genre
        count = int(c)
print prevGenre, '\t', count
