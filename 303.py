def f(n):
	i=n
	v=[int(x) for x in str(i)]
	fi=filter(lambda x: x > 2, v)
	while len(list(fi))!=0:
		i+=n
		v=[int(x) for x in str(i)]
		fi=filter(lambda x: x > 2, v)
	return i
s=0
for i in range(1,10001):
	s+=(f(i)/i)
print(s)