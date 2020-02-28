#!/bin/python
import sympy
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""
lim = 2000000
sum = 0
if(lim % 2 == 0):
	lim = lim - 1
while(lim > 2):
	if(sympy.isprime(lim)):
		sum = sum + lim
	lim = lim - 2
print(sum + 2) #142913828922