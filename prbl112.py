#!/bin/python
#from joblib import Parallel, delayed
#import multiprocessing
def isIncreasingNumber(number):
	word=str(number)
	digits=[int(x) for x in word[1:]]
	filtered=list(filter(lambda x: x < int(word[0]), digits))
	while(len(filtered)==0 and len(word)>0):
		word=word[1:]
		digits=[int(x) for x in word[1:]]
		filtered=list(filter(lambda x: x < int(word[0]), digits))
	return len(word)==0
def isDecreasingNumber(number):
	word=str(number)
	digits=[int(x) for x in word[1:]]
	filtered=list(filter(lambda x: x > int(word[0]), digits))
	while(len(filtered)==0 and len(word)>0):
		word=word[1:]
		digits=[int(x) for x in word[1:]]
		filtered=list(filter(lambda x: x > int(word[0]), digits))
	return len(word)==0
def isBouncyNumber(number):
	return (not isIncreasingNumber(number)) and (not isDecreasingNumber(number))
i,cIncreasing, cDecreasing, cBouncy, p =1,0,0,0,0.0
while(p!=0.99):
	if(isIncreasingNumber(i)):
		cIncreasing+=1
	elif(isDecreasingNumber(i)):
		cDecreasing+=1
	else:
		cBouncy+=1
	i+=1
	p=cBouncy/(cIncreasing+cDecreasing+cBouncy)
print(p,i-1)

#parallel
# what are your inputs, and what operation do you want to 
# perform on each input. For example...
#inputs = range(10) 
#def processInput(i):
#    return i * i
# 
#num_cores = multiprocessing.cpu_count()
#results = Parallel(n_jobs=num_cores)(delayed(processInput)(i) for i in inputs)
#
#print(num_cores)
#print(results)