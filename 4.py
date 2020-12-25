import sys
sys.path.append("C:/Users/paulo/Documents/ProjectEuler")
from _str import *
lst = list(range(100,1000))
maior = -1
for x in lst:
    for y in lst:
        if x*y > maior and IsPalindrome(str(x*y)):
            maior = x*y
print(maior)