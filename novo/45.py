import sys
import math
def IsPentagonalNumber(number):
	delta = (24 * number + 1)
	sq = math.sqrt(delta)
	s1 = int((sq+1)/6)
	r = int(0.5*s1*(3*s1-1))
	return r == number
for n in range(144,1000000):
	num = n * (2*n - 1)
	if(IsPentagonalNumber(num)):
		print(num, n)
		sys.exit()