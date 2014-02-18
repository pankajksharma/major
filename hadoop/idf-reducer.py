#! /usr/bin/env python
import sys
from math import log
N = 500.0
presentWord = None
presentWordCount = 0

for word in sys.stdin:
	word = word.strip()
	if presentWord and word != presentWord:
		print "%s\t%f" %(presentWord, log(N/presentWordCount))
		presentWordCount = 0
	presentWord = word
	presentWordCount += 1
print "%s\t%f" %(word, log(N/presentWordCount))