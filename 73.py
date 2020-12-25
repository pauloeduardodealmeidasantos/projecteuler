import math
import functools
from functools import cmp_to_key
class Fracao:
	def __init__(self,numerador,denominador):
		self.denominador=denominador
		self.numerador=numerador
	def __str__(self):
		return str(self.numerador)+"/"+str(self.denominador)
def compare(f1, f2):
	if(f1.denominador==f2.denominador):
		if(f1.numerador<f2.numerador):
			return -1
		elif(f1.numerador>f2.numerador):
			return 1
		else:
			return 0
	else:
		d=f1.denominador*f2.denominador
		n1=f1.numerador*f2.denominador
		n2=f2.numerador*f1.denominador
		f3=Fracao(n1,d)
		f4=Fracao(n2,d)
		return compare(f3,f4)
def EstaNoLimite(f):
	return compare(f,menor)==1 and compare(f,maior)==-1
lim=12000
menor=Fracao(1,3)
maior=Fracao(1,2)
cont=0
i=0
for d in range(2,lim+1):
	for n in filter(lambda x: math.gcd(x,d)==1, range(1,d)):
		f=Fracao(n,d)
		if(EstaNoLimite(f)):
			cont+=1
print('#####')
print(cont)