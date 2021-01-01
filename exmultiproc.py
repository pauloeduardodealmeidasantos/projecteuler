import multiprocessing
from joblib import Parallel, delayed
def CheckEven(n):
	temp = n 
	while(temp > 0): 
		digit = temp % 10
		if(digit % 2 == 0):
			return False
		temp = temp // 10
	return True
def IsReverseNumber(n):
	if(n%10==0):
		return False
	else:
		r=int(str(n)[::-1])
		return CheckEven(r+n)
lim=10**2
num_cores = multiprocessing.cpu_count()
chunk = 10**5
i=0
count=0
while(i < lim):
	ret=Parallel(n_jobs=num_cores)(delayed(IsReverseNumber)(i) for i in
	range(i,i+chunk))
	ret=list(filter(lambda x: x, ret))
	count+=len(ret)
	print(i,i+chunk,count)
	i+=chunk
