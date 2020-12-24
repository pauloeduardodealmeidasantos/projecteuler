s = 2
a = 1
b = 2
while b < 4*(10**6):
    a,b=b,(a+b)
    if b % 2 == 0:
        s+=b
print(s)
