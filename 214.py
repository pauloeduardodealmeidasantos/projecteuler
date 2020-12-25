import sympy
def GetReminder(Pn,n):
	r = (((Pn-1)**n) + ((Pn+1)**n)) % (Pn*Pn)
	return r
def IsChain25(n):
	t=n
	t=sympy.totient(t)
	i=1
	while(i<=25 and t!=1):
		i+=1
		t=sympy.totient(t)
	return (i+1)==25
v=[]
n=2
while(n<4*(10**7)):
	print(n)
	n=sympy.nextprime(n)
	if(IsChain25(n)):
		v.append(n)
		print('################')
print('#######################')
print(v)
print(sum(v))
#print(GetReminder(5,3))
#lim=10**10
#n=1
#Pn=2
#r=GetReminder(Pn,n)
#while(r<lim):
#	print(n,Pn,GetReminder(Pn,n))
#	Pn=sympy.nextprime(Pn)
#	n+=1
#	r=r=GetReminder(Pn,n)
#print('##################')
#print(n,Pn,GetReminder(Pn,n))
#Pn=sympy.nextprime(Pn)
#n+=1
#print(n,Pn,GetReminder(Pn,n))
