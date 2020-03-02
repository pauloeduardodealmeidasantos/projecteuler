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
uplim = 28123
dwlim = 12
abLst = []
lst = []
ret = []
for i in range(dwlim,uplim+1, 2):
	if(SumProperDivisors(i)>i):
		abLst.append(i)
for i in range(945,uplim+1, 2):
	if(SumProperDivisors(i)>i):
		abLst.append(i)
for i in range(0,len(abLst)):
	for j in range(i,len(abLst)):
		lst.append(abLst[i]+abLst[j])
a = range(1, uplim+1)
w = [x for x in a if x not in lst]
print(sum(w))#demora demais mas não vou otimizar mais.