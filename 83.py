v=[]
f = open("/home/paulo/src/projecteuler/mtx.txt", "r")
for line in f:
	aux=[]
	for n in line.split(","):
		aux.append(int(n))
	v.append(aux)
f.close()
print(v)