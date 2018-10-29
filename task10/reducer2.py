#!/usr/bin/env python2
import sys

prevTitle = None
year = None
crewID = None

def isInt(value):
    try: 
        int(value)
        return True
    except ValueError:
        return False

for line in sys.stdin:
    title, value = line.strip().split('\t')
    
    if title != prevTitle:
        year = None

    if isInt(value):
        year = int(value)
    else:
        crewID = value

    if title == prevTitle and year >= 2010 and year <= 2018 and year != None:
        print crewID

    prevTitle = title
