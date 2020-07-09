#!/bin/python
iterations_limit=50
limit_search=10000
def isPalindromeString(str):
	return str == str[::-1]
def isPalindromeNumber(number):
	return isPalindromeString(str(number))
def reverseNumber(number):
	return int(str(number)[::-1])
def isLychrelNumber(number):
	cont = 1
	aux = number + reverseNumber(number)
	while(cont < iterations_limit and not isPalindromeNumber(aux)):
		aux += reverseNumber(aux)
		cont+=1
	return not (cont < iterations_limit and isPalindromeNumber(aux))
lst=[]
for i in range(1,limit_search):
	if(isLychrelNumber(i)):
		lst.append(i)
print(len(lst))