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
	lst = set(lst)
	return lst
def isNotTrivial(i,j):
	uNumerador = i % 10
	dNumerador = (i - uNumerador)/10
	uDenominador = j % 10
	dDenominador = (j - uDenominador)/10
	if(uNumerador == dDenominador and uDenominador != 0 and (i / j==dNumerador / uDenominador )):
		return True
	return False
	'''
	if(n%10==0 or m%10==0):
		return False
	d1 = ProperDivisors(n)
	d2 = ProperDivisors(m)
	for i in d1:
		for j in d2:
			if(i==j):
				return False
	return True
	'''
p = 1
for i in range(10,100):
	for j in range(i+1,100):
		if(isNotTrivial(i,j)):
			print(i,j)
			p = p * (j/i)
print(p)