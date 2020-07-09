#!/bin/python
lst1=[]
lst89=[]
def SumSqDigits(n):
	return sum([int(x)*int(x) for x in str(n)])
def GetSumSqDigitsSequence(n):
	sq = n
	while(sq!=1 and sq!=89):
		sq=SumSqDigits(sq)
	if(sq==1):
		lst1.append(n)
	elif(sq==89):
		lst89.append(n)
for i in range(1,10000000):
	print(i)
	GetSumSqDigitsSequence(i)
print(len(lst1))
print(len(lst89))