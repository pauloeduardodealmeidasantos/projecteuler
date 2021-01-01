import sympy
import math
ret=0
def SqProperDivisors(n):
	d = sympy.divisors(n)
	s = sum([x**2 for x in d])
	return s
for i in range(1,64000000):
	r = SqProperDivisors(i)
	if math.sqrt(r).is_integer():
		ret+=i
print(ret)