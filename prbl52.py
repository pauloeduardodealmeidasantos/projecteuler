#!/bin/python
def isProblem52Complete(x):
	s1=sorted(''+str(x))
	s2=sorted(''+str(x*2))
	s3=sorted(''+str(x*3))
	s4=sorted(''+str(x*4))
	s5=sorted(''+str(x*5))
	s6=sorted(''+str(x*6))
	return s1==s2==s3==s4==s5==s6
x=1
while(not isProblem52Complete(x)):
	x+=1
print(x)