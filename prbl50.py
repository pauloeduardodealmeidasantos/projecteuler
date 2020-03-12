#!/bin/python
from sympy import *
import sys
import sympy
import math
pot = 6
maior = 65
maximo = 10**pot
lst = list()
lstprimerange = list(sieve.primerange(2,maximo))
for position in range(0,len(lstprimerange)):
	limDivisor = int((lstprimerange[position]+1)/2)
	sublist = list(filter(lambda x: x <= limDivisor, lstprimerange))
	if(sum(sublist) <= maximo and len(sublist) > maior):
		lst.append(sublist)
		if(sympy.isprime(sum(sublist)) and len(sublist) > maior):
			maior = len(sublist)
lst = list(filter(lambda x: len(x) > maior, lst))
while(len(lst)>1):
	mlst = lst[-1]
	for j in range(0,len(mlst)):
		plst = mlst[j:]
		s = sum(plst)
		if(len(plst) > maior and sympy.isprime(s)):
			maior=len(plst)
			print('maior parcial::'+str(maior)+'prime:'+str(s))
		while(len(plst) > maior):
			plst = plst[:-1]
			s = sum(plst)
			if(len(plst) > maior and sympy.isprime(s)):
				maior=len(plst)
				print('maior parcial::'+str(maior)+'prime:'+str(s))
	lst.remove(mlst)
	lst=list(filter(lambda x: len(x) > maior, lst))
print('maior::'+str(maior))