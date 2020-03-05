#!/bin/python
import sys
import primefac
def GetNumberDistinctPrimes(num):
	return len(set(primefac.primefac(num)))
RAZAO = 2
continueLooping = True
count = 10
res = list()
while(continueLooping):
	lst = list()
	for num in range(count,RAZAO):
		d = GetNumberDistinctPrimes(num)
		print(count,num,d)
		if(d in lst):
			continueLooping = False
			break
			print(consecs)
		lst.append(d)
	count +=1	