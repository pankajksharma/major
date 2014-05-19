#! /usr/bin/env python
import sys

for line in sys.stdin:
	line = line.strip()
	parts = line.split('\t')
	if len(parts) != 3:
		continue
	doc = parts[0]
	term = parts[1]
	tfreq = int(parts[2])

	if term == '0':
		wSum = float(tfreq)
	else:
		print "{0}\t{1}\t{2}".format(term, doc, tfreq/wSum)
