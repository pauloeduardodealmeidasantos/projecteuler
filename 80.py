import math
from bigfloat import *
with precision(750):
	s=0
	for i in range(1,101):
		if not math.sqrt(i).is_integer():
			r = sqrt(i)
			d = str(r).replace(".","")
			s += sum([int(x) for x in d[:100]])
print(s)