def p(L,n):
	j=0
	c=0
	while c!= n:
		while str(L) != str(2**j)[:len(str(L))]:
			j+=1
		c+=1
		j+=1
	return j-1
print(p(123,1))
print(p(12,2))
print(p(12,3))
print(p(12,4))
print(p(12,5))
print(p(12,6))
print(p(123,678910))
