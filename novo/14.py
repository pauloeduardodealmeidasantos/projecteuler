def HowManyNumberInSeq(n):
	ret = 1
	aux = n;
	while(aux != 1):
		if(aux%2==0):
			aux = aux / 2
		else:
			aux = 1 + 3*aux
		ret = ret +1
	return ret
maior = 0;
numero = 0;
x = 0
for i in range(1,1000000):
	x=HowManyNumberInSeq(i)
	if(x>maior):
		maior=x
		numero=i
print(numero)