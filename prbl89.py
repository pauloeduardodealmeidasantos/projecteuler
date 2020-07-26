#!/bin/python
import math

class NumRomano:
	def __init__(self,original):
		self.original=original
		self.dec=RomanToDecimal(original)
	def __str__(self):
		return str(self.original)

def RomanToDecimal(st):
	soma=0
	i=0
	while(i<len(st)):
		L=st[i]
		v=LetterToNumber(L)
		if(i>0):
			Lb=st[i-1]
			if((L=='V' or L=='X') and Lb=='I'):
				v-=2
			elif((L=='L' or L=='C') and Lb=='X'):
				v-=20
			if((L=='D' or L=='M') and Lb=='C'):
				v-=200
		#print(L,v)
		soma+=v
		i+=1
	return soma

def LetterToNumber(L):
	if(L=='I'):
		return 1
	elif(L=='V'):
		return 5
	elif(L=='X'):
		return 10
	elif(L=='L'):
		return 50
	elif(L=='C'):
		return 100
	elif(L=='D'):
		return 500
	elif(L=='M'):
		return 1000
	else:
		return 0

lst=[]
soma=0
f = open("p89.txt", "r")
for fline in f:
	line=fline.replace('\n','')
	r=NumRomano(line)
	lst.append(r)
f.close()
for r in lst:
	s=r.original.replace('DCCCC','YY').replace('LXXXX','YY').replace('VIIII','YY').replace('CCCC','YY').replace('XXXX','YY').replace('IIII','YY')
	soma+=(len(r.original)-len(s))
print(soma)