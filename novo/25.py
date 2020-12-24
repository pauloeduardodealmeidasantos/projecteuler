l = 1000
i = 2
n = 1
aux = 1
f = 1
while(len(str(f)) < l):
	i = i+1
	aux = n
	n = f
	f = f+aux
	#print(f,i)
print(i)