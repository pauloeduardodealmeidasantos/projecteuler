import sympy
#n*n + na + b tem que ser primo
# a<1000 b <=1000 n começa em 0
#primeiro detalhe: se n for 0, b tem que ser primo. então b sempre é primo
def equacao(a,b,n):
	return n*n + a*n + b
	#return n*n + n + 41
bLst = list(sympy.primerange(2,1000))
aLst = list(range(-1000,1000))
lst = []
y = 0
ret = (0,0)
m = 0
n = 0
for b in bLst:
	for a in aLst:
		n = 0
		r = equacao(a,b,n)
		while(sympy.isprime(r)):
			n+=1
			r = equacao(a,b,n)
		if(n > m):
			m = n
			ret=(b,a)
			print(r,a,b,n)

print('###################')
print(m)
print(ret)
print(len(bLst))
print('###################')
