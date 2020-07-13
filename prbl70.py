#!/bin/python
import sympy
import sys
def isPermutation(x,y):
	s1=sorted(''+str(x))
	s2=sorted(''+str(y))
	return s1==s2
menor=100
sn=0
for n in range(2,10**7):
	totient_n = sympy.totient(n)
	q=n/totient_n
	if(q<menor):
		if(isPermutation(n,totient_n)):
			sn=n
			menor=q
			print(n,totient_n,q)
print(sn,menor)
	