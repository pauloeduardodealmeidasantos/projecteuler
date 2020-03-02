#!/bin/python
def SomaTermosCantos(n):
	an = n*n - 3 * (n-1)
	sn = ((n*n) + an) * 2
	return sn
max = 1001;
n = max;
sum = 0;
while (n > 1):
	sum += SomaTermosCantos(n)
	n -= 2
sum+=1
print(sum)