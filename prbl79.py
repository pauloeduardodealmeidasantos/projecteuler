#!/bin/python
#distinct=[]
#dic1=dict()
#dic2=dict()
#dic3=dict()
#for i in [0, 1, 2, 3, 6, 7, 8, 9]:
	#dic1[i]=0
	#dic2[i]=0
	#dic3[i]=0
f = open("p079.txt", "r")
for fline in f:
	line=fline.replace('\n','')
	#a=int(line[0])
	#b=int(line[1])
	#c=int(line[2])
	#dic1[a]+=1
	#dic2[b]+=1
	#dic3[c]+=1
	#distinct.append(int(line[0]))
	#distinct.append(int(line[1]))
	#distinct.append(int(line[2]))
	#print(line.replace('\n',''))
#distinct=list(set(distinct))
#print(distinct)
# [0, 1, 2, 3, 6, 7, 8, 9] # 8 casas
#[(7, 21), (3, 12), (6, 8), (1, 6), (2, 2), (8, 1), (0, 0), (9, 0)]
#[(1, 15), (2, 10), (6, 10), (8, 9), (9, 4), (3, 2), (0, 0), (7, 0)]
#[(9, 17), (0, 16), (8, 6), (2, 5), (6, 5), (1, 1), (3, 0), (7, 0)]
# 7 nunca apareceu no meio e fim. começa com 7!
# 0 nunca apareceu no meio e no começo. final 0!
# 9 só aparece no meio seguido de 0. termina 90
#dic1=sorted(dic1.items(), key=lambda x: x[1], reverse=True)
#dic2=sorted(dic2.items(), key=lambda x: x[1], reverse=True)
#dic3=sorted(dic3.items(), key=lambda x: x[1], reverse=True)
#print(dic1)
#print(dic2)
#print(dic3)
73162890