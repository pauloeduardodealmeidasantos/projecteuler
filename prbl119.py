#!/bin/python
def FindPowerSumOfDigits(n):
	s=sum([int(x) for x in str(n)])
	i=0
	while(s!=1 and s**i < n):
		i+=1
	if(s**i==n):
		return i
	else:
		return -1
v=[]
i=1
while(len(v)<50):
	i+=1
	p=2
	while(p<50):
		exp=i**p
		s=sum([int(x) for x in str(exp)])
		if(s==i):
			print(len(v),i,p,s,exp)
			v.append((i,p))
		p+=1
print('#################')
print(v)