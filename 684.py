v = []
a = 0
b = 1
v.append(a)
while len(v) < 90:
	a,b=b,(a+b)
	v.append(b)
print(v)
