#!/bin/python
import sympy
def GetNumbersInDiagonal(length):
	lim = length**2
	step = length-1
	mySet = (lim,lim-step,lim-(step*2),lim-(step*3))
	return list(filter(lambda x: sympy.isprime(x), mySet))
lst=[]
length=1
p=1
while p > 0.1:
	length+=2
	lst = lst + GetNumbersInDiagonal(length)
	p = len(lst) / ((length*2) - 1)
	print(length,p)
#print(length,p)
#print(lst)
#length=8
#lst=[]
#lst.append(1)
#for i in range(3,length+1,2):
#	for n in GetNumbersInDiagonal(i):
#		lst.append(n)
#	print(GetNumbersInDiagonal(i))
#total=len(lst)
#lst=list(filter(lambda x: sympy.isprime(x), lst))
#print(len(lst)/total)