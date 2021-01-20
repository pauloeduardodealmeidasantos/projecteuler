def PosibleSteps(v,m,n,steps):
	ret=[]
	p=(0,0)
	#left
	if n-1 >= 0 and (m,n-1) not in steps:
		p = (m,n-1)
		if not p in steps:
			ret.append(p)
	#right
	if n+1 <= len(v)-1:
		p = (m,n+1)
		if not p in steps:
			ret.append(p)
	#up
	if m-1 >= 0:
		p = (m-1,n)
		if not p in steps:
			ret.append(p)
	#down
	if m+1 <= len(v)-1:
		p = (m+1,n)
		if not p in steps:
			ret.append(p)
	return ret
def CalcSum(v,m,n,steps):
	if cache[m][n] != -1:
		return cache[m][n]
	if m==len(v)-1 and m==n:
		return v[m][n]
	new_steps=steps.copy()
	new_steps.append((m,n))
	posible_steps = PosibleSteps(v,m,n,new_steps)
	menor = 10**6
	for p in posible_steps:
		soma = CalcSum(v,p[0],p[1],new_steps)
		if soma < menor:
			menor = soma
	cache[m][n] = menor+v[m][n]
	return menor+v[m][n]
v=[]
cache = []
import sys
sys.setrecursionlimit(sys.getrecursionlimit()*10)
f = open("/home/paulo/src/projecteuler/mtx.txt", "r") #2297
#f = open("/home/paulo/src/projecteuler/p083_matrix.txt", "r") #425185
for line in f:
	aux=[]
	aux1=[]
	for n in line.split(","):
		aux.append(int(n))
		aux1.append(-1)
	v.append(aux)
	cache.append(aux1)
f.close()
l = list()
s = CalcSum(v,0,0,l)
print(s)