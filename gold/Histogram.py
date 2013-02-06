from collections import *
def histogram(L): 
	d = defaultdict(int)
	for x in L: 
		d[x] += 1
	return d
