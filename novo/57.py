cache=[]
class Fracao:
	def __init__(self,numerador,denominador):
		self.denominador=denominador
		self.numerador=numerador
	def __str__(self):
		return str(self.numerador)+"/"+str(self.denominador)
def SomaFracao(f1,f2):
	denominador=f1.denominador*f2.denominador
	numerador=(f1.numerador*f2.denominador)+(f2.numerador*f1.denominador)
	f=Fracao(numerador,denominador)
	return f
def MultiplicaFracao(f1,f2):
	denominador=f1.denominador*f2.denominador
	numerador=f1.numerador*f2.numerador
	f=Fracao(numerador,denominador)
	return f
def DivideFracao(f1,f2):
	f3=Fracao(f2.denominador,f2.numerador)
	return MultiplicaFracao(f1,f3)
def SomaContinuaRaizDois(n):
	return SomaFracao(Fracao(1,1),FracaoRaizDois(n))
def FracaoRaizDois(n):
	if(len(cache)>=n): #RecursionError: maximum recursion depth exceeded
		return cache[n-1]
	if(n==1):
		f=Fracao(1,2)
		cache.append(f)
		return f
	else:
		f=SomaFracao(Fracao(2,1),FracaoRaizDois(n-1))
		f=DivideFracao(Fracao(1,1),f)
		cache.append(f)
		return f
count=0
print('##########')
for i in range(1,1000):
	x=SomaContinuaRaizDois(i)
	v=str(x).split("/")
	if(len(v[0])>len(v[1])):
		count+=1
print(count)