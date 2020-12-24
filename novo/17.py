vZeroNine = ['one','two','three','four','five','six','seven','eight','nine']
vElevenNineteen = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
vTwentyToNinety = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
v = []
for i in vZeroNine:
	v.append(i)
	print (i+":"+str(len(i)))
for i in vElevenNineteen:
	v.append(i)
	print (i +":"+str(len(i)))
for i in vTwentyToNinety:
	v.append(i)
	print (i)
	for j in vZeroNine:
		st = str(i) + '-' + str(j)
		v.append(st)
		print(st+":"+str(len(st)))
for k in vZeroNine:
	x = str(k) + ' hundred'
	v.append(x)
	print(x+":"+str(len(x)))
	for g in vZeroNine:
		o =x + ' and ' + str(g)
		v.append(o)
		print(o+":"+str(len(o)))
	for h in vElevenNineteen:
		o =x + ' and ' + str(h)
		v.append(o)
		print(o+":"+str(len(o)))
	for i in vTwentyToNinety:
		y = x + ' and ' + str(i)
		v.append(y)
		print(y+":"+str(len(y)))
		for j in vZeroNine:
			st = x + ' and ' + str(i) + '-' + str(j)
			v.append(st)
			print(st+":"+str(len(st)))
v.append('one thousand')
soma = 0
for i in v:
	soma = soma + len(i.replace(' ','').replace('-',''))
print(soma)