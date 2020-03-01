#!/bin/python
import primefac
import sys
def ProperDivisors(n):
	lst = list(primefac.primefac(n))
	for i in range(1,len(lst)):
		for j in lst[i:]:
			if(n % (lst[i-1]*j) == 0):
				lst.append(lst[i-1]*j)
	while(n in lst):
		lst.remove(n)
	lst.append(1)
	lst = set(lst)
	return lst
def SumProperDivisors(n):
	return sum(ProperDivisors(n))
d = dict()
for j in range(2,10000):
	st= str(j)
	v = SumProperDivisors(j)
	d[st]=v
for i in d.items():
	for item in d.items():
		k1 =int(item[0])
		v1 = int(item[1])
		k2 = int(i[0])
		v2 = int(i[1])
		if(k1==v2 and k2==v1 and k1!=k2):
			print(k1,k2)