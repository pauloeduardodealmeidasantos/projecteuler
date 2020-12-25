from sympy import *
import sympy
import math
lst=[]
def squarefree(n):
	primes=primerange(2,1+math.floor(math.sqrt(n)))
	for p in primes:
		if(n % (p*p) == 0):
			return False
	return True
def printPascal(n) : 
	for line in range(0, n) : 
		for i in range(0, line + 1) :
			lst.append(binomialCoeff(line, i))
def binomialCoeff(n, k) : 
    res = 1
    if (k > n - k) : 
        k = n - k 
    for i in range(0 , k) : 
        res = res * (n - i) 
        res = res // (i + 1) 
    return res 
printPascal(51) 
lst=list(set(lst))
sqfree = list(filter(lambda x: squarefree(x), lst))
print(sum(sqfree))