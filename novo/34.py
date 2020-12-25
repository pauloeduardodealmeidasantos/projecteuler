import math
import numpy
v = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
lst = []
max = v[-1]*5
min = 3
for i in range(min,max):
	sum = 0
	for p in str(i):
		index = int(p)
		sum += v[index]
	if(int(i) == sum):
		lst.append(int(i))
print(lst)