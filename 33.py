def isNotTrivial(i,j):
	uNumerador = i % 10
	dNumerador = (i - uNumerador)/10
	uDenominador = j % 10
	dDenominador = (j - uDenominador)/10
	if(uNumerador == dDenominador and uDenominador != 0 and (i / j==dNumerador / uDenominador )):
		return True
	return False
p = 1
for i in range(10,100):
	for j in range(i+1,100):
		if(isNotTrivial(i,j)):
			print(i,j)
			p = p * (j/i)
print(p)