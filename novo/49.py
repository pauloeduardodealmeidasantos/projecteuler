import sympy
from sympy import *
def IsPermut(n,m):
	s1 = list(set(str(n)))
	s2 = list(set(str(m)))
	return s1==s2
lst = list(sieve.primerange(1000,9999))
perm = list()
for i in range(0,len(lst)):
	for j in range(i+1,len(lst)):
		for k in range(j+1,len(lst)):
			n1 = lst[i]
			n2 = lst[j]
			n3 = lst[k]
			if(n3 - n2 == 3330 and n3 - n2 == n2 - n1 and IsPermut(n1,n2) and IsPermut(n2,n3)):
				print(n1,n2,n3)