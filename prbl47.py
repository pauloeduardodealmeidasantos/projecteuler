#!/bin/python
from sympy import *
import sympy
import sys
def numberDistinctPrimes(num,lst):
	count = 0
	ret = list()
	for elem in lst:
		if(num % elem == 0):
			count += 1
			ret.append(elem)
			if(count > 4):
				return [ret,count]
	return [ret,count]
lst = list(sieve.primerange(1,5))
i = 2
j = 3
k = 4
w = 5
while(true):
	if(lst[-1] < i+4):
		lst.append(nextprime(lst[-1], ith=1))
	if(numberDistinctPrimes(i,lst)[1] == 4 and numberDistinctPrimes(j,lst)[1] == 4 and numberDistinctPrimes(k,lst)[1] == 4 and numberDistinctPrimes(w,lst)[1] == 4):
		print(i,j, k,w)
		sys.exit()
	i+=1
	j+=1
	k+=1
	w+=1
	