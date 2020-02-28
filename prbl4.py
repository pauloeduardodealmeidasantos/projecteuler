#!/bin/python
"""
A palindromic number reads the same both ways. The largest palindrome made from the product
of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
maior = 0;
lim = 1000;
aux = 0;
for x in range(lim):
	for y in range(lim):
			aux = x * y
			if(str(aux)==str(aux)[::-1]):
				if (aux > maior):
					maior = aux;
print(maior) #906609