#!/bin/python
import math
min = 2
max = 100
v=[]
s = set()
for a in range(min,max+1):
	for b in range(min,max+1):
		v.append(math.pow(a,b))
s = set(v)
print(len(s))