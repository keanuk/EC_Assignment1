import sys

for line in sys.stdin:
	line = line.strip()
	words = line.split()
	print 'lc', 1
	for word in words:
		print 'wc', 1
