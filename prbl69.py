#!/bin/python
import sympy
maior=0
sn=0
for n in range(2,10**6):
	totient_n = sympy.totient(n)
	q=n/totient_n
	if(q>maior):
		maior=q
		sn=n
		#print(n,totient_n,q)
print(sn,maior)