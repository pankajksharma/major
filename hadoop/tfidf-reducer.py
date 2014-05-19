#! /usr/bin/env python
import sys

for line in sys.stdin:
	line = line.strip()
	parts = line.split('\t')
	if len(parts) != 3:
		break
	if parts[1] == '-1':
		idf = float(parts[2])
	else:
		word = parts[0]
		doc = parts[1]
		tf = float(parts[2])
		print "{0}\t{1}\t{2}".format(doc, word, tf*idf)