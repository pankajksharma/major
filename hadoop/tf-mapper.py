#! /usr/bin/env python
import sys,re,hashlib

for line in sys.stdin:
	line = line.strip()
	m = hashlib.md5()
	m.update(line)
	words = re.findall(r'[\d]+:[\d]+', line)
	mhexdigest = m.hexdigest()
	wordSum = sum([int(word.split(':')[1]) for word in words])
	print "{0}\t{1}\t{2}".format(mhexdigest, "0", wordSum)
	for word in words:
		w,f = word.split(':')
		print "{0}\t{1}\t{2}".format(mhexdigest, w, f)