#!/bin/python
from sympy import *
import sympy
import sys
def IsGoldbach(i,lst):
	for j in lst:
		lim = int((i - j)/2)
		for k in range(1,lim+1):
			n = j + (2*k*k)
			if(i==n):
				return True
	return False
escape = False
i = 33
lst = list(sieve.primerange(1,i))
while(not escape):
	if(lst[-1] < i):
		lst.append(nextprime(lst[-1], ith=1))
	if(not sympy.isprime(i)):
		if(not IsGoldbach(i,lst)):
			print(i)
			sys.exit()
	i+=2