import sympy
lim = 2000000
sum = 0
if(lim % 2 == 0):
	lim = lim - 1
while(lim > 2):
	if(sympy.isprime(lim)):
		sum = sum + lim
	lim = lim - 2
print(sum + 2)