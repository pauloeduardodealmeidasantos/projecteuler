def Is145(n):
	if n % 10 == 0:
		return False
	r = int(str(n)[::-1])
	lst = [int(x) for x in str(n+r)]
	for d in lst:
		if d % 2 == 0:
			return False
	return True
i=10
c=0
while i < 10**9:
	if Is145(i):
		c+=1
	i+=1
print(c)