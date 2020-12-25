#!/bin/python
def MenorDois(x,y):
	if(x<y):
		return x
	else:
		return y
def CalcSum(v,m,n,up):
	lim = len(v) - 1
	if(cache[m][n] != -1):
		return cache[m][n]
	elif(n==lim):
		cache[m][n]=v[m][n]
		return cache[m][n]
	elif(m==0 and n < lim):
		r = CalcSum(v,m,n+1,False)
		if(up):
			cache[m][n]=r+v[m][n]
			return cache[m][n]
		else:
			d = CalcSum(v,m+1,n,False)
			menor = MenorDois(r,d)
			cache[m][n]=menor+v[m][n]
			return cache[m][n]
	elif(m==lim and n < lim):
		r = CalcSum(v,m,n+1,False)
		if(up):
			cache[m][n]=r+v[m][n]
			return cache[m][n]
		else:
			u = CalcSum(v,m-1,n,True)
			menor = MenorDois(r,u)
			cache[m][n]=menor+v[m][n]
			return cache[m][n]
	else:
		r = CalcSum(v,m,n+1,False)
		if(up):
			u = CalcSum(v,m-1,n,True)
			menor = MenorDois(r,u)
			cache[m][n]=menor+v[m][n]
			return cache[m][n]
		else:
			u = CalcSum(v,m-1,n,True)
			d = CalcSum(v,m+1,n,False)
			menor = MenorDois(MenorDois(r,u),d)
			cache[m][n]=menor+v[m][n]
			return cache[m][n]

v=[]
cache = []
#f = open("mtx.txt", "r")
f = open("C:/Users/paulo/Documents/ProjectEuler/p082_matrix.txt", "r")
#280967
for line in f:
	w = line.split(",")
	aux=[]
	for n in w:
		aux.append(int(n))
	v.append(aux)
f.close()
for i in range(0,len(v)):
	cache.append([])
	for j in range(0,len(v)):
		cache[i].append(-1)
s = 10**10
for i in range(0,len(v)):
	x = CalcSum(v,i,0,False)
	if(x < s):
		s = x
print(s)