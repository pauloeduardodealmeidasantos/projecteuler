def printPascal(n) : 
	c=0
	for line in range(0, n) : 
		for i in range(0, line + 1) :
			#lst.append(binomialCoeff(line, i))
			r = binomialCoeff(line, i)
			if r % 7 != 0:
				c+=1
	print(c)
def binomialCoeff(n, k) : 
    res = 1
    if (k > n - k) : 
        k = n - k 
    for i in range(0 , k) : 
        res = res * (n - i) 
        res = res // (i + 1) 
    return res
printPascal(10**9)