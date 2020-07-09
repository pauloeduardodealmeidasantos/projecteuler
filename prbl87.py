#!/bin/python
import math
import sympy
from sympy import *
import sys
p=[]
lim=50
lim=lim * 10**6
r = math.floor(math.sqrt(lim));
v = list(sieve.primerange(1,r))
for x in v:
	for y in list(filter(lambda q: q**3 <= lim - x**2, v)):
		for z in list(filter(lambda q: q**4 <= lim - x**2 - y**3, v)):
			if((x**2+y**3+z**4)<=lim):
				p.append((x**2+y**3+z**4))
s=set(p)
p=list(s)
print(p)
print(len(p))