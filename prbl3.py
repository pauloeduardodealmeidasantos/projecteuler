#!/bin/python
import sympy 
import math
"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
lim = 600851475143
r = math.ceil(math.sqrt(lim));
while r > 1:
	if(lim % r == 0 and sympy.isprime(r)):
		break
	r-=1
print(r) #6857
