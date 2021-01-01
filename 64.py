import math
from bigfloat import *
with precision(750):
	for i in range(1,10001):
		if not math.sqrt(i).is_integer():
			r = sqrt(i)
			print(i,r)