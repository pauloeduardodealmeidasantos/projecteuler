#!/bin/python
import math
import numpy
v = math.factorial(100)
vStr = str(v).replace('0','')
s = 0
for i in range(0,len(vStr)):
	s+=int(vStr[i])
print(s)
