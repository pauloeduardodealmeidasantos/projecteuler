a = (2,5)
b = (3,7)
while a[1] < 10**6:
	a, b = (a[0]+b[0],a[1]+b[1]), b
	print(a)