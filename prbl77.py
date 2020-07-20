#!/bin/python
import sympy
lim=10
def CountWays(lim):
	sizes=range(1,lim)
	sizes=list(sympy.primerange(2,lim))
	ways=[]
	for i in range(0,lim+2):
		ways.append(0)
	ways[0]=1
	for i in range(0,len(sizes)):
		for j in range(sizes[i],lim+1):
			ways[j] += ways[j-sizes[i]]
	#print(ways[lim])
	return ways[lim]
while(CountWays(lim)<5000):
	lim=lim+1
print(lim)