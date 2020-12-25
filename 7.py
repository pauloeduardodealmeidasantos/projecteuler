import sympy
p = 2
i = 1
while i < 10001:
    p = sympy.nextprime(p)
    i+=1
print(p)