verdadeiros = []
falsos = []
for L in range(12,1500001):
	print(L)
	count=0
	for a in range(1,L):
		for b in range(a+1,L):
			for c in range(b+1,L):
				if (a*a)+(b*b)==(c*c):
					count+=1
					if count > 1:
						break
	if count == 2:
		falsos.append(L)
	else:
		verdadeiros.append(L)
print(verdadeiros)
print(falsos)
print(len(verdadeiros),len(falsos))