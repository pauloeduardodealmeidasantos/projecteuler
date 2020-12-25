def CalcSum(v,m,n):
	lim = len(v) - 1
	if(cache[m][n] != -1):
		return cache[m][n]
	if(n==lim and m==lim):
		cache[m][n] = v[m][n]
		return cache[m][n]
	elif(m==lim and n < lim):
		cache[m][n] = v[m][n]+CalcSum(v,m,n+1)
		return cache[m][n]
	elif(n==lim and m < lim):
		cache[m][n] = v[m][n]+CalcSum(v,m+1,n)
		return cache[m][n]
	else:
		r = CalcSum(v,m,n+1)
		d = CalcSum(v,m+1,n)
		if(r < d):
			cache[m][n] = v[m][n]+r
			return cache[m][n]
		else:
			cache[m][n] = v[m][n]+d
			return cache[m][n]
v=[]
cache = []
f = open("C:/Users/paulo/Documents/ProjectEuler/p081_matrix.txt", "r")
for line in f:
	w = line.split(",")
	aux=[]
	aux1=[]
	for n in w:
		aux.append(int(n))
		aux1.append(-1)
	v.append(aux)
	cache.append(aux1)
f.close()
s = CalcSum(v,0,0)
print(s)