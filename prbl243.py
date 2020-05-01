#!/bin/python
import primefac
def ResilienceOfDenominator(d):
	lst = list(range(1,d))
	fatr = list(primefac.primefac(d)) # contem repeat
	sfatr = set(fatr) # eliminou repeat
	for num in sfatr:
		lst = list(filter(lambda x: x % num != 0, lst))
	#print(lst)
	#print(sfatr)
	return len(lst)

numerador=15499
#15499 / 94744
numero = 94744
r = ResilienceOfDenominator(numero)
while(r % numerador != 0):
	numero = numero + numero
	r = ResilienceOfDenominator(numero+1)
	print(r, numero)
print(numero)
#não funciona ainda.
