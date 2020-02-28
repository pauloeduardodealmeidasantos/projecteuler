#!/bin/python
import numpy
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 
without any remainder.
What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?
"""
#v = range(6,11)
v = range(11,21)
mmc = numpy.lcm.reduce(v)
print (mmc) #232792560