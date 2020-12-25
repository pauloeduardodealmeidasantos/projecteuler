#!/bin/python
import shapely
from shapely.geometry import Polygon
from shapely.geometry import Point
f = open("p102_triangles.txt", "r")
pt = Point(0,0)
c=0
for line in f:
	w = line.replace('\n','').split(",")
	plg = Polygon([[int(w[0]), int(w[1])], [int(w[2]), int(w[3])], [int(w[4]), int(w[5])]])
	if(plg.contains(pt)):
		c+=1
print(c)
