import sympy
abNumbers = list()
res=list()
for i in range(0,28124):
    res.append(False)
    if sum(sympy.divisors(i))-i>i:
        abNumbers.append(i)
combinations = list()
for i in range(0,len(abNumbers)-1):
    for j in range(0,len(abNumbers)-1):
        if(abNumbers[i]+abNumbers[j]<28124):
            res[abNumbers[i]+abNumbers[j]]=True
s=0
for i in range(0,28124):
    if res[i]:
        s+=i
print(s)