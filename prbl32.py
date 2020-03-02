#!/bin/python
def isPanDigital(a,b,c):
	v = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
	s = str(a)+str(b)+str(c)
	s = sorted(s)
	return s == v
def isPanDigitalVet(w):
	return isPanDigital(w[0],w[1],w[2])
lst=[]
for i in range(10,100):
	for j in range(10,100):
		w = [i,j,i*j]
		if(isPanDigitalVet(w)):
			lst.append(w)
for i in range(10,100):
	for j in range(100,1000):
		w = [i,j,i*j]
		if(isPanDigitalVet(w)):
			lst.append(w)
for i in range(1,10000):
	for j in range(1,10):
		w = [i,j,i*j]
		if(isPanDigitalVet(w)):
			lst.append(w)
q = []
print('#####################')
for i in lst:
	q.append(i[2])
print(set(q),sum(set(q)))
print('#####################')

