import sympy
def SumProperDivisors(n):
	d = sympy.divisors(n)
	s = sum(d) - n
	return s
uplim = 28123
dwlim = 12
abLst = []
lst = []
ret = []
for i in range(dwlim,uplim+1, 2):
	if(SumProperDivisors(i)>i):
		abLst.append(i)
for i in range(945,uplim+1, 2):
	if(SumProperDivisors(i)>i):
		abLst.append(i)
for i in range(0,len(abLst)):
	for j in range(i,len(abLst)):
		lst.append(abLst[i]+abLst[j])
a = range(1, uplim+1)
w = [x for x in a if x not in lst]
print(sum(w))#demora demais mas não vou otimizar mais.