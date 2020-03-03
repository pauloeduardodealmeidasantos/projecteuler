#!/bin/python
def isPanDigital(w):
	v = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
	s = ''+w
	s = sorted(s)
	return s == v
def GetSomaString(w):
	soma =0
	for i in w:
		soma += int(i)
	return soma
maior = -1
for i in range(1,20000):
	cont = 1
	som = 0
	s = ''
	while(som<45):
		m = i * cont
		s = s + str(m)
		som += GetSomaString(str(m))
		cont+=1
		if(som==45 and isPanDigital(s)):
			if(int(s)>maior):
				maior=int(s)
				print(i,som,s)
print(maior) #932718654