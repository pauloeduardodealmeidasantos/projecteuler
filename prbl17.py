#!/bin/python
"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) 
contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""
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
print('one thousand')
print(len(''.join(v)))
print(len(v))
soma = 0
for i in v:
	soma = soma + len(i.replace(' ','').replace('-',''))
print(soma)