#!/bin/python
import sympy
def GetReminder(Pn,n):
	r = (((Pn-1)**n) + ((Pn+1)**n)) % (Pn*Pn)
	return r
#print(GetReminder(5,3))
lim=10**10
n=1
Pn=2
r=GetReminder(Pn,n)
while(r<lim):
	print(n,Pn,GetReminder(Pn,n))
	Pn=sympy.nextprime(Pn)
	n+=1
	r=r=GetReminder(Pn,n)
print('##################')
print(n,Pn,GetReminder(Pn,n))
Pn=sympy.nextprime(Pn)
n+=1
print(n,Pn,GetReminder(Pn,n))
