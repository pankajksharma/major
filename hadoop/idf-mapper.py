#! /usr/bin/env python
import sys,re

for line in sys.stdin:
	for sv in re.findall(r'[\d]+:[\d]+', line):
		print sv.split(':')[0]