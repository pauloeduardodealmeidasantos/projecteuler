#!/bin/python
import math
#potencia sempre simplifica com log
#https://www.todamateria.com.br/propriedades-dos-logaritmos/
#log b^c = c log b
v=[]
f = open("p099_base_exp.txt", "r")
for line in f:
	w = line.rstrip().split(",")
	v.append((int(w[0]),int(w[1])))
maior = 0
el=0
for e in v:
	#print(e[0]**e[1])
	plog = math.log(e[0],10) * e[1]
	if(plog>maior):
		maior=plog
		el=e
print(maior)
print(el)