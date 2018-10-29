#!/usr/bin/env python2
import sys

titleDict = {}

for line in sys.stdin:
    line = line.strip().split('\t')
    if len(line) > 6:
        if line[5] != '\N' and int(line[5]) >= 2010 and int(line[5]) <= 2018:
            # print line[0], '\t', line[5]
            if line[0] in titleDict:
                titleDict[line[0]] = titleDict[line[0]] + ',' + str(line[5])
            else:
                titleDict[line[0]] = str(line[5])
    else:
        for title in line[5].strip().split(','):
            # print title, '\t', line[0]
            if title in titleDict:
                titleDict[title] = titleDict[title] + ',' + line[0]
            else: 
                titleDict[title] = line[0]
print titleDict