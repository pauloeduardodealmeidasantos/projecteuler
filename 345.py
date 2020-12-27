def CalcSum(v,m,n):
	lim = len(v) - 1
	if(cache[m][n] != -1):
		return cache[m][n]

v =  [[ 7  ,53 ,183 ,439, 863]
,[497 ,383 ,563 , 79 ,973]
,[287 , 63 ,343 ,169 ,583]
,[627 ,343 ,773 ,959 ,943]
,[767 ,473 ,103 ,699 ,303]]
cache=[]
for i in range(0,len(v)):
	cache.append([])
	for j in range(0,len(v)):
		cache[i].append(-1)