import numpy
def isPalindroma(str):
	return str == str[::-1]
def GetBinario(num):
	ret = numpy.binary_repr(num)
	if(ret[0]=='0'):
		ṕrint(ret)
	return ret
v1 = []
for i in range(1,1000000):
	if(isPalindroma(str(i)) and isPalindroma(GetBinario(i))):
		v1.append(i)
print(v1,len(v1), sum(v1))