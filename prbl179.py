#!/bin/python
from sympy import divisors, divisor_count

#print(divisor_count(14))
i=2
count=0
divisor_anterior=divisor_count(2)
while(i<10**7):
	print(i)
	f=divisor_count(i+1)
	if(divisor_anterior==f):
		count+=1
	i+=1
	divisor_anterior=f
print(count,i)