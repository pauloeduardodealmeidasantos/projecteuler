import sympy
from sympy import *
def GetFilteredList(lst,n):
	filtered=list(filter(lambda x: sympy.isprime(int(str(n)+str(x))) and sympy.isprime(int(str(x)+str(n))), lst))
	return filtered
lst = list(sieve.primerange(3,10**4))
for a in lst:
	sub1=GetFilteredList(lst,a)
	for b in sub1:
		sub2=GetFilteredList(sub1,b)
		for c in sub2:
			sub3=GetFilteredList(sub2,c)
			for d in sub3:
				sub4=GetFilteredList(sub3,d)
				for e in sub4:
					print(a,b,c,d,e)