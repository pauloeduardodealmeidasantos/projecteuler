import sympy
from functools import reduce
def rad(n):
	r=list(sympy.primefactors(n))
	r=list(set(r))
	r=reduce((lambda x, y: x * y), r)
	return r
lst=[]
lim=100000
#lim=10
lst.append([1,1])
for n in range(2,lim+1):
	lst.append([n,rad(n)])
#sort
lst=sorted(lst, key=lambda x: (x[1], x[0]))
for el in lst:
	print("n: %d; rad(n): %d" %(el[0],el[1]))
print('#############')
print(lst[9999])