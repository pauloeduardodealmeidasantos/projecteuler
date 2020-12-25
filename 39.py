lim = 1000
maior = -1
count = 0
for p in range(1,lim+1):
	count = 0
	for i in range(1,p+1):
		for j in range(i+1,p+1-i):
			for k in range(j+1,p+1-i-j):
				if(i+j+k==p and i**2+j**2==k**2):
					count += 1
	if(count > maior):
		maior = count
		print(p,'::',count)
		

	
	
