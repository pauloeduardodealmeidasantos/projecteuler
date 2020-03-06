#!/bin/python
from sympy import *
import sys
import sympy
lst = list(sieve.primerange(2,10**3))
init = len(lst)
for i in range(init,3,-1):
	for j in range(1,len(lst)):
		k = lst[-1*j]
		c = 0
		s = 0
		while(s<=k):
			sublist = lst[c:]
			sublist = sublist[:i]
			s = sum(sublist)
			c+=1
			if(s==k):
				print(sublist,c,s,k)
				sys.exit()
