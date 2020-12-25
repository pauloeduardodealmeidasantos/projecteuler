class Card:
	def __init__(self,st_value,suit):
		self.st_value=st_value
		self.value=self.GetValue(st_value)
		self.suit=suit
	def GetValue(self,st_value):
		ret=0
		try:
			ret=int(st_value)
		except:
			if(st_value=='T'):
				ret=10
			elif(st_value=='J'):
				ret=11
			elif(st_value=='Q'):
				ret=12
			elif(st_value=='K'):
				ret=13
			elif(st_value=='A'):
				ret=14
		return ret
class Hand:
	def __init__(self):
		self.deck=[]
		self.outcome = 0
	def add_card(self,c):
		self.deck.append(c)
		self.deck.sort(key=lambda x: x.value)
	def __str__(self):
		s=""
		for i in self.deck:
			s+=i.st_value+i.suit+";"
		return s
def CalcOutcome(h):
	isConsecutive=True
	isSameSuit=True
	distinctValues = list(set([x.value for x in h.deck]))
	v=[]
	for val in distinctValues:
		aux=list(filter(lambda x: x.value == val, h.deck))
		v.append(len(aux))
	#Definir se todos são mesmo naipe
	isSameSuit=len(set([x.suit for x in h.deck]))==1
	#Definir se todos são consecutivos
	#isConsecutive=len(set([x.value for x in h.deck]))==5
	for i in range(0,4):
		isConsecutive = isConsecutive and h.deck[i+1].value-h.deck[i].value==1
	#Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
	if(h.deck[0].value==10 and isSameSuit and isConsecutive):
		h.outcome=9
	#Straight Flush: All cards are consecutive values of same suit.
	elif(isSameSuit and isConsecutive):
		h.outcome=8
	#Four of a Kind: Four cards of the same value.
	elif(len(set([x.value for x in h.deck[:4]]))==1 or len(set([x.value for x in h.deck[-4:]]))==1):
		h.outcome=7
	#Full House: Three of a kind and a pair.
	elif(3 in v and 2 in v):
		h.outcome=6
	#Flush: All cards of the same suit.
	elif(isSameSuit):
		h.outcome=5
	#Straight: All cards are consecutive values.
	elif(isConsecutive):
		h.outcome=4
	#Three of a Kind: Three cards of the same value.
	elif(3 in v):
		h.outcome=3
	#Two Pairs: Two different pairs.
	elif(len(list(filter(lambda x: x==2, v)))==2):
		h.outcome=2
	#One Pair: Two cards of the same value.
	elif(2 in v):
		h.outcome=1
	else:
		h.outcome=0
def CompareHands(h1,h2):
	#https://www.pokerstars.com/br/poker/games/rules/hand-rankings/?no_redirect=1 
	if(h1.outcome==h2.outcome):
		if(h1.outcome==8):
			return h1.deck[4].value>h2.deck[4].value
		elif(h1.outcome==7):
			v1=GetRepeatedCard(h1,4)
			v2=GetRepeatedCard(h2,4)
			return v1[0]>v2[0]
		elif(h1.outcome==6):
			v1=GetRepeatedCard(h1,3)
			v2=GetRepeatedCard(h2,3)
			return v1[0]>v2[0]
		elif(h1.outcome==5):
			i=4
			while(i >= 0 and h1.deck[i].value==h2.deck[i].value):
				i=i-1
			return h1.deck[i].value>h2.deck[i].value
		elif(h1.outcome==4):
			return h1.deck[4].value>h2.deck[4].value
		elif(h1.outcome==3):
			v1=GetRepeatedCard(h1,3)
			v2=GetRepeatedCard(h2,3)
			return v1[0]>v2[0]
		elif(h1.outcome==2):
			v1=GetRepeatedCard(h1,2)
			v2=GetRepeatedCard(h2,2)
			if(v1[0]!=v2[0]):
				return v1[0]>v2[0]
			else:
				return v1[2]>v2[2]
		elif(h1.outcome==1):
			v1=GetRepeatedCard(h1,2)
			v2=GetRepeatedCard(h2,2)
			if(v1[0]!=v2[0]):
				return v1[0]>v2[0]
			else:
				i=4
				while(i >= 0 and h1.deck[i].value==h2.deck[i].value):
					i=i-1
				return h1.deck[i].value>h2.deck[i].value
		elif(h1.outcome==0):
			i=4
			while(i >= 0 and h1.deck[i].value==h2.deck[i].value):
				i=i-1
			return h1.deck[i].value>h2.deck[i].value
	else:
		return h1.outcome > h2.outcome
def GetRepeatedCard(h,n):
	ret=[]
	if(n==4):
		if(len(set([x.value for x in h.deck[:4]]))==1):
			ret.append(h.deck[0].value)
		else:
			ret.append(h.deck[4].value)
	elif(n==3):
		if(len(set([x.value for x in h.deck[:3]]))==1):
			ret.append(h.deck[0].value)
		elif(len(set([x.value for x in h.deck[1:4]]))==1):
			ret.append(h.deck[1].value)
		elif(len(set([x.value for x in h.deck[2:5]]))==1):
			ret.append(h.deck[2].value)
		else:
			ret.append(0)
	elif(n==2):
		con=-1
		for i in h.deck:
			con=0
			for j in h.deck:
				if(j.value==i.value):
					con+=1
			if(con==2):
				ret.append(i.value)
	else:
		ret.append(0)
	return ret
f = open("C:/Users/paulo/Documents/ProjectEuler/p054_poker.txt", "r")
count=0
contaLinha=0
for line in f:
	contaLinha+=1
	w = line.replace('/n','').split(" ")
	first5=w[:5]
	last5=w[-5:]
	h1=Hand()
	h2=Hand()
	for it in first5:
		h1.add_card(Card(it[0],it[1]))
	for it in last5:
		h2.add_card(Card(it[0],it[1]))
	CalcOutcome(h1)
	CalcOutcome(h2)
	if(CompareHands(h1,h2)):
		count+=1
print(count)