#!/bin/python
def DigitalSum(number):
	v=sum([int(x) for x in str(number)])
	return v
maior=0
x=0
for a in range(1,100):
	for b in range(1,100):
		x=DigitalSum(a**b)
		if(x>maior):
			maior=x
print(maior)