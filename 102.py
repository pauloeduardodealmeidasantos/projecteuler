def is_left(P0, P1, P2):
    return (P1[0] - P0[0]) * (P2[1] - P0[1]) - (P2[0] - P0[0]) * (P1[1] - P0[1])
def wn_PnPoly(P, V): #(=0 only if P is outside V[])
    wn = 0   # the winding number counter

    # repeat the first vertex at end
    V = tuple(V[:]) + (V[0],)

    # loop through all edges of the polygon
    for i in range(len(V)-1):     # edge from V[i] to V[i+1]
        if V[i][1] <= P[1]:        # start y <= P[1]
            if V[i+1][1] > P[1]:     # an upward crossing
                if is_left(V[i], V[i+1], P) > 0: # P left of edge
                    wn += 1           # have a valid up intersect
        else:                      # start y > P[1] (no test needed)
            if V[i+1][1] <= P[1]:    # a downward crossing
                if is_left(V[i], V[i+1], P) < 0: # P right of edge
                    wn -= 1           # have a valid down intersect
    return wn
p = (0,0)
v = [[0,0],[0,0],[0,0]]
c=0
#v = [[-340,495],[-153,-910],[835,-947]]
#print(wn_PnPoly(p,v))
#v = [[-175,41],[-421,-714],[574,-645]]
#print(wn_PnPoly(p,v))
f = open("/home/paulo/src/projecteuler/p102_triangles.txt", "r")
for line in f:
	#print(line)
	w = line.replace('/n','').split(",")
	v[0] = [int(w[0]),int(w[1])]
	v[1] = [int(w[2]),int(w[3])]
	v[2] = [int(w[4]),int(w[5])]
	if wn_PnPoly(p,v) != 0:
		c+=1
f.close()
print(c)
