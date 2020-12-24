import sympy
t = 1
n = 1
while sympy.divisor_count(t) < 501:
    n+=1
    t = int(n * (n+1) * 0.5)
print(t)

    