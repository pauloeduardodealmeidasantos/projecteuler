#!/bin/python
import sympy
def GeraCircular(p):
	count = 0 
	ret = []
	ret.append(str(p))
	aux = ''
	rot = ''+str(p)
	aux = rot[0] # pega primeiro elemento
	rot = rot[1:]+(aux)
	while(rot != str(p)):
		ret.append(rot)
		aux = rot[0] # pega primeiro elemento
		rot = rot[1:]+(aux)
	return ret
def isCircular(p):
	sum = 0
	for l in str(p):
		sum += int(l)
		if(int(l) % 2 == 0):
			return False
		if(int(l) == 5):
			return False
	if(sum % 3 == 0):
		return False
	#após testes triviais, vamos rot
	rot = GeraCircular(p)
	for r in rot:
		if(not sympy.isprime(int(r))):
			return False
	return True
lst = list(sympy.primerange(2,13))
vet = list(sympy.primerange(13,1000000))
for p in vet:
	if(isCircular(p)):
		lst.append(p)
print('###################')
print(lst,len(lst))
print('###################')