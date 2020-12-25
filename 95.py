#!/bin/python
from sympy import proper_divisors

def ListaAmicableChain(n):
	ret=[]
	ret.append(n)
	aux=GetSumDivisors(n)
	while(not aux in ret and aux <= 10**6):
		ret.append(aux)
		aux=GetSumDivisors(aux)
	if(GetSumDivisors(ret[-1])!=n):
		ret=[]
	return ret

def GetSumDivisors(n):
	if(SumDivisors[n]==0):
		soma = sum(proper_divisors(n))
		SumDivisors[n]=soma
	return SumDivisors[n]

SumDivisors=[]
for i in range(0,10**6):
	SumDivisors.append(0)
SumDivisors[0]=-1
SumDivisors[1]=-1
mList=[]
for i in range(28,10**6):
	r=ListaAmicableChain(i)
	if(len(r) > len(mList)):
		mList=r
print('#############')
print(min(mList),mList)