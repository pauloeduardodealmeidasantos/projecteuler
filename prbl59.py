#!/bin/python
def GeneratePossibleKeys():
	r=[]
	letters="abcdefghijklmnopqrstuvwxyz"
	for l1 in letters:
		for l2 in letters:
			for l3 in letters:
				r.append(l1+l2+l3)
	return r
f = open("p059_cipher.txt", "r")
v=[int(x) for x in f.readline().split(",")]
possible_keys=GeneratePossibleKeys()
for k in possible_keys:
	phrase=""
	for i in range(0,100):
		phrase+=chr(v[i]^ord(k[i % 3]))
	#print(phrase+"#"+k[0]+k[1]+k[2])
### exp
k="exp"
text=""
for i in range(0,len(v)):
		text+=chr(v[i]^ord(k[i % 3]))
print(text)
s=[ord(x) for x in text]
print(sum(s))
#print(65^asckey)
#print(32^asckey)
#print(65^asckey)
#/print(107^asckey)
#for c in v:
#	print(chr(c))
#print(ord("A"))
#print(ord("k"))
#print(65^42)
#print(107^42)
'''
dic=dict()
for cchar in v:
	if(cchar in dic):
		dic[cchar]+=1
	else:
		dic[cchar]=1
for x,y in sorted(dic.items(), key=lambda x: x[1], reverse=True):
	print(str(x)+": "+str((y/len(v))*100)+"%")
'''
