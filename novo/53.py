from sympy.functions.combinatorial.numbers import nC
c=0
for n in range (1,101):
	for r in range(0,n+1):
		if(nC(n,r) > 10**6):
			c+=1
			print(n,r)
print(c)