#!/bin/python
import sys
#funcoes auxiliares
def GetDoisPrimeirosDigitos(n):
	return str(n)[:2]
def GetDoisUltimosDigitos(n):
	return str(n)[2:]
def IsTriangulo(n):
	return n in triangulos
def IsQuadrado(n):
	return n in quadrados
def IsPentagono(n):
	return n in pentagonos
def IsHexagono(n):
	return n in hexagonos
def IsHeptagono(n):
	return n in heptagonos
def IsOctogono(n):
	return n in octogonos
def IsProblema61(v):
	t=len(list(filter(lambda x: IsTriangulo(x), v)))
	q=len(list(filter(lambda x: IsQuadrado(x), v)))
	p=len(list(filter(lambda x: IsPentagono(x), v)))
	h6=len(list(filter(lambda x: IsHexagono(x), v)))
	h7=len(list(filter(lambda x: IsHeptagono(x), v)))
	o=len(list(filter(lambda x: IsOctogono(x), v)))
	#todo hexago eh triangulo!
	return t==2 and q==1 and p==1 and h6==1 and h7==1 and o==1
triangulos=[int(n*(n+1)*0.5) for n in range(1,10000)]
quadrados=[int(n*n) for n in range(1,10000)]
pentagonos=[int(n*((3*n)-1)*0.5) for n in range(1,10000)]
hexagonos=[int(n*((2*n)-1)) for n in range(1,10000)]
heptagonos=[int(n*((5*n)-3)*0.5) for n in range(1,10000)]
octogonos=[int(n*((3*n)-2)) for n in range(1,10000)]
#filtrar
triangulos=list(filter(lambda x: len(str(x))==4, triangulos))
quadrados=list(filter(lambda x: len(str(x))==4, quadrados))
pentagonos=list(filter(lambda x: len(str(x))==4, pentagonos))
hexagonos=list(filter(lambda x: len(str(x))==4, hexagonos))
heptagonos=list(filter(lambda x: len(str(x))==4, heptagonos))
octogonos=list(filter(lambda x: len(str(x))==4, octogonos))
#processar
lst=list(set(triangulos+quadrados+pentagonos+hexagonos+heptagonos+octogonos))
conjuntos=[]
for a in triangulos	:
	for b in list(filter(lambda x: GetDoisUltimosDigitos(a)==GetDoisPrimeirosDigitos(x), lst)):
		for c in list(filter(lambda x: GetDoisUltimosDigitos(b)==GetDoisPrimeirosDigitos(x), lst)):
			for d in list(filter(lambda x: GetDoisUltimosDigitos(c)==GetDoisPrimeirosDigitos(x), lst)):
				for e in list(filter(lambda x: GetDoisUltimosDigitos(d)==GetDoisPrimeirosDigitos(x), lst)):
					for f in list(filter(lambda x: GetDoisUltimosDigitos(e)==GetDoisPrimeirosDigitos(x) and GetDoisPrimeirosDigitos(a)==GetDoisUltimosDigitos(x), lst)):
						conjuntos.append([a,b,c,d,e,f])
for i in conjuntos:
	if(IsProblema61(i)):
		print(i,sum(i))