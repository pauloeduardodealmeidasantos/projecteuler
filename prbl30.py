#!/bin/python
import math
pot = 5
min = 2
max = 9**pot*10 #o lim superior é completamente arbitrário
v = []
for num in range(min,max):
	d = [int(math.pow(int(x),pot)) for x in str(num)]
	if(num == sum(d)):
		v.append(num)
print(v)
print(sum(v))