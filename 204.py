import sympy
maximo = 15
hamm = 5
cont = 1
lst = list(sympy.primerange(1,hamm+1))
err = list(filter(lambda x: x > hamm, lst))
lst = list(filter(lambda x: x <= hamm, lst))
#print(err)
#print(lst)
for p in lst:
	print(p)
