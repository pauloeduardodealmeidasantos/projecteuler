#!/bin/python
import sympy
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.
What is the 10 001st prime number?

"""
lim = 10001;
count = 2;
n = 3;
while(count < lim):
	n+=2
	if(sympy.isprime(n)):
		count+=1
print(n) #104743