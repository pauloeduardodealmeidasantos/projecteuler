import math
v=[]
f = open("C:/Users/paulo/Documents/ProjectEuler/p099_base_exp.txt", "r")
for line in f:
	w = line.rstrip().split(",")
	v.append((int(w[0]),int(w[1])))
maior = 0
el=0
for e in v:
	plog = math.log(e[0],10) * e[1]
	if(plog>maior):
		maior=plog
		el=e
print(maior)
print(el)