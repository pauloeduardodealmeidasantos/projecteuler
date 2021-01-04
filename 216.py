import sympy
p=0
n=1
while n <= 50000000:
	t=(2*(n**2)) - 1
	if sympy.isprime(t):
		p+=1
	n+=1
print(p)