dicp = dict()
dicc = dict()
for a in range(1,5):
	for b in range(1,5):
		for c in range(1,5):
			for d in range(1,5):
				for e in range(1,5):
					for f in range(1,5):
						for g in range(1,5):
							for h in range(1,5):
								for i in range(1,5):
									n = a+b+c+d+e+f+g+h+i
									if n in dicp:
										dicp[n]+=1
									else:
										dicp[n]=1
for a in range(1,7):
	for b in range(1,7):
		for c in range(1,7):
			for d in range(1,7):
				for e in range(1,7):
					for f in range(1,7):
						n = a+b+c+d+e+f
						if n in dicc:
							dicc[n]+=1
						else:
							dicc[n]=1
w=0
t=(4**9)*(6**6)
for x0,y0 in dicp.items():
	for x1,y1 in dicc.items():
		if x0 > x1:
			w+=y0*y1
print(w,t,w/t)