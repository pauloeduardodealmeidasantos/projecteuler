#!/bin/python
#https://en.wikipedia.org/wiki/Pentagonal_number
import math
def IsPentagonalNumber(number):
	delta = (24 * number + 1)
	sq = math.sqrt(delta)
	s1 = int((sq+1)/6)
	r = int(0.5*s1*(3*s1-1))
	return r == number
def roda(limite):
	for i in range(1,2268):
		pi = int((3*i-1)*i/2)
		for k in range(1,i):
			pk = int((3*k-1)*k/2)
			if(IsPentagonalNumber(pi+pk) and IsPentagonalNumber(abs(pk-pi))):
				print(pi,pk)
				return [i,k,pi,pk]
limite = 10000
r = roda(10000)
print(r)
		