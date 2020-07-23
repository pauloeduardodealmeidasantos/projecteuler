#!/bin/python
import math
def TestNoveDigitos(n):
	s=str(n)
	return s[0]=="1" and s[2]=="2" and s[4]=="3" and s[6]=="4" and s[8]=="5" and s[10]=="6" and s[12]=="7" and s[14]=="8" and s[16]=="9" 
maximo = 19293949596979899
rmax = math.floor(math.sqrt(maximo))
lst=range(1,rmax+1)
lst=list(filter(lambda x: (x % 10 == 3 or x % 10 == 7) and math.floor(math.log10(x**2)) == math.floor(math.log10(maximo)), lst))
#print(rmax,maximo)
print(len(lst))
print(TestNoveDigitos(maximo),maximo)
i=0
while(not TestNoveDigitos(lst[i]**2)):
	i+=1
print(lst[i],lst[i]**2)