def isPanDigital(w):
	v = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
	s = ''+w
	s = sorted(s)
	return s == v
def isPanDigitalPrbl104(number):
	s=str(number)
	return isPanDigital(s[-9:]) and isPanDigital(s[:9])
a, b, c = 0, 1, 0
while not isPanDigitalPrbl104(a):
	a, b = b, a+b
	c+=1
print('###')
print(a)
print(c)
#329468