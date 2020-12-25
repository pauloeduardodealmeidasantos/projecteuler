import sys
def IsPermutation(a,b):
	x=''+str(a)
	y=''+str(b)
	return a!=b and sorted(x) == sorted(y)
cubics=[int(n**3) for n in range(100,10000)]
for a in cubics:
	sub1=list(filter(lambda x: len(str(x))==len(str(a)) and IsPermutation(a,x), cubics))
	for b in sub1:
		sub2=list(filter(lambda x: len(str(x))==len(str(b)) and IsPermutation(b,x), sub1))
		for c in sub2:
			sub3=list(filter(lambda x: len(str(x))==len(str(c)) and IsPermutation(c,x), sub2))
			for d in sub3:
				sub4=list(filter(lambda x: len(str(x))==len(str(d)) and IsPermutation(d,x), sub3))
				for e in sub4:
					print(a,b,c,d,e)
					sys.exit()