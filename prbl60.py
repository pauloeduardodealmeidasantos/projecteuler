#!/bin/python
import sympy
from sympy import *
lst = list(sieve.primerange(1,999))
lst.remove(2)
lst.remove(5)
print(lst)