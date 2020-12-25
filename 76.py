lim=100
sizes=range(1,lim)
ways=[]
for i in range(0,lim+2):
	ways.append(0)
ways[0]=1
for i in range(0,len(sizes)):
	for j in range(sizes[i],lim+1):
		ways[j] += ways[j-sizes[i]]
print(ways[lim])
print(ways)