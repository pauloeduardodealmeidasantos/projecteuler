#!/bin/python
import itertools
v = [0,1,2,3,4,5,6,7,8,9]
#v = [0,1,2]
p = list(itertools.permutations(v))
print(len(p))
print(p[999999])