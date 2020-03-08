#!/bin/python
from sympy import *
import sys
import sympy
import math
def MaiorSubLista(sublista,n):
	for j in range(0,len(sublista)):
		pList = sublista[j:]
		s = sum(pList)
		c = maior
		while(len(pList) > maior and s > n):
			pList = pList[:-1]
			s = sum(pList)
			c+=1
		if(s==n):
			return len(pList)
	return -1
pot = 2
maior = -1
lstprimerange = list(sieve.primerange(2,10**pot))
for position in range(len(lstprimerange)-1,3,-1):
	print('##########################################')
	print(lstprimerange[position])
	print('##########################################')
	limit = int((lstprimerange[position]+1)/2)
	sublist = list(filter(lambda x: x < limit, lstprimerange))
	while(sublist[-1]+sublist[-2] > lstprimerange[position] and sum(sublist) <= lstprimerange[position]):
		limit = int((sublist[-1]+1)/2)
		sublist = list(filter(lambda x: x < limit, sublist))
	ret = MaiorSubLista(sublist,lstprimerange[position])
	if(ret > maior):
		print(ret,lstprimerange[position])
		maior = ret
print('maior::'+str(maior))