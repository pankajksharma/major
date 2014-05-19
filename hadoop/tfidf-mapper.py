#! /usr/bin/env python
import sys

for line in sys.stdin:
	line = line.strip()
	parts = line.split('\t')
	if len(parts) != 2 and len(parts) != 3:
		continue
	if len(parts) == 2:
		print "{0}\t{1}\t{2}".format(parts[0], "-1", parts[1])
	else:
		print "{0}\t{1}\t{2}".format(*parts)