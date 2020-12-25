import sympy
lst_numbers = list()
s=0
for i in range(0,10001):
    lst_numbers.append(False)
for i in range(1,10001):
    if not lst_numbers[i]:
        n = sum(sympy.divisors(i, True))
        m = sum(sympy.divisors(n - i, True))
        if n == m and i != n-i:
            lst_numbers[i]=True
            lst_numbers[n-i]=True
for i in range(1,10001):
    if lst_numbers[i]:
        print(i)
        s+=i
print(s)