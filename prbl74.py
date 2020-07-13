#!/bin/python
import math
vFatorial = [math.factorial(x) for x in range(0,10)]
def SumOfDigitFactorial(number):
	return sum([vFatorial[int(x)] for x in str(number)])
def CountChainMember(number):
	chain=[]
	aux=number
	while(not (aux in chain) and len(chain)<60):
		chain.append(aux)
		aux=SumOfDigitFactorial(aux)
	return len(chain)
count=0
#CountChainMember(69)
for i in range(1,10**6):
	if(CountChainMember(i)==60):
		count+=1
print(count)