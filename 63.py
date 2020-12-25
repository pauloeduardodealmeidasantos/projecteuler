#!/bin/python
v=[1,2,3,4,5,6,7,8,9]
i=1
count=9
w=[x**i for x in v]
f=list(filter(lambda x: len(str(x))==i, w))
while(len(f)>0):
	print(f)
	i+=1
	w=[x**i for x in v]
	f=list(filter(lambda x: len(str(x))==i, w))
	count+=len(f)
print(count)