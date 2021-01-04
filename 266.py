from sympy import *
import math
def psr(n):
	q=math.floor(math.sqrt(n))
	while n % q != 0:
		q-=1
	return q
#print(psr(12))
#print(psr(3102))
primes = list(sieve.primerange(2,190))
p=1
for i in primes:
	p*=i
ret=psr(p)
print(ret % (10**16))