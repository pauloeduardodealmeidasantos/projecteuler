import sympy
import itertools
def isPanDigital(w,n):
	v = ['1', '2', '3', '4', '5', '6', '7', '8', '9'][:n]
	s = ''+w
	s = sorted(s)
	return s == v
v = [1,2,3,4,5,6,7,8,9]
obj=list()
lst = list()
for num in v:
	lst = lst + list(itertools.permutations(v[:num]))
for item in lst:
	if(isPanDigital(''.join(map(str, item)),len(item)) and sympy.isprime(int(''.join(map(str, item))))):
		obj.append(int(''.join(map(str, item))))
for i in obj:
	print(i)
print('########')
print(max(obj))