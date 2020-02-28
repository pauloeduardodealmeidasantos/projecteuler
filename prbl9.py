#!/bin/python
import numpy
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

"""
muito útil na solução. fonte wikipedia https://en.wikipedia.org/wiki/Pythagorean_triple
A Pythagorean triple consists of three positive integers a, b, and c, such that a2 + b2 = c2. 
Such a triple is commonly written (a, b, c), and a well-known example is (3, 4, 5). 
If (a, b, c) is a Pythagorean triple, then so is (ka, kb, kc) for any positive integer k. 
a = t(2.m + 1),b = t(2.m^2 + 2.m),  c = t(2.m^2 + 2.m +1).
http://www.rpm.org.br/cdrpm/7/12.htm
todas as idéias acima geram números pitogáricos. só não geram a condição para solucionar o problema 9!
"""
lst = []
for i in range(1,1000):
	for j in range(i+1,1000):
		for k in range(j+1,1000):
                    if(i+j+k==1000 and i**2 + j**2 == k**2):
                        print(i,j,k)


		


	
	
