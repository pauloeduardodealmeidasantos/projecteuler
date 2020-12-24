import numpy
v = []
aux=[]
f = open("c:/p067_triangle.txt", "r")
for line in f:
	w = line.split(" ")
	aux=[]
	for n in w:
		aux.append(int(n))
	v.append(aux)
f.close()
v = numpy.flip(v,0)
def Maximo(a,b):
	if(a > b):
		return a
	else:
		return b
s1 = 0
s2 = 0
for i in range(1,len(v)):
	for j in range(0, len(v[i])):
		s1 = v[i][j] + v[i-1][j]
		s2 = v[i][j] + v[i-1][j+1]
		v[i][j] = Maximo(s1,s2)
print(v[-1])