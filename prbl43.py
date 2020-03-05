#!/bin/python
import itertools
def IsPanDigital(w):
	v = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
	s = ''+w
	s = sorted(s)
	return s == v
def IsProblem43(w):
	s = ''+str(w)
	if((int(s[3])) % 2 != 0):
		return False
	if((int(s[2:5])) % 3 != 0):
		return False
	if((int(s[5])) % 5 != 0):
		return False
	if((int(s[4:7])) % 7 != 0):
		return False
	if((int(s[5:8])) % 11 != 0):
		return False
	if((int(s[6:9])) % 13 != 0):
		return False
	if((int(s[7:10])) % 17 != 0):
		return False
	return True
v = [0,1,2,3,4,5,6,7,8,9]
obj=list()
st=''
lst = list(itertools.permutations(v))
for item in lst:
	st=''.join(map(str, item))
	if(IsPanDigital(st) and IsProblem43(st)):
		obj.append(st)
for i in obj:
	print(i)
print('########')
