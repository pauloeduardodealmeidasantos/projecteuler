import datetime
first = 1901
last = 2000
count = 0
mes = 0
while(first <= last):
	mes = 1
	while(mes <= 12):
		d = datetime.datetime(first, mes, 1)
		if(d.weekday()==6):
			count+=1
		mes+=1
	first+=1
print(count)