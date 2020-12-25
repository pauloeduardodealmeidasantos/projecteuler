#!/bin/python
import sympy
s=0
lim=10**6
for i in range(2,lim+1):
	totient_n = sympy.totient(i)
	s+=totient_n
print(s)