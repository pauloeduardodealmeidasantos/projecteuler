#!/bin/python
import sympy
def isTruncable(n):
	aux = ''+str(n)
	while(len(aux) > 1):
		aux = aux[1:]
		if(not sympy.isprime(int(aux))):
			return False
	aux = ''+str(n)
	while(len(aux) > 1):
		aux = aux[:-1]
		if(not sympy.isprime(int(aux))):
			return False
	return True
v = []
x = 7
count = 0
while(count<11):
	x = sympy.nextprime(x)
	if(isTruncable(x)):
		v.append(x)
		count += 1
print(sum(v))
	
