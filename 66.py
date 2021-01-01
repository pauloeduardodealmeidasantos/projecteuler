import math
def solvePell(n):
    x = int(math.sqrt(n))
    y, z, r = x, 1, x << 1
    e1, e2 = 1, 0
    f1, f2 = 0, 1
    while True:
        y = r * z - y
        z = (n - y * y) // z
        r = (x + y) // z
 
        e1, e2 = e2, e1 + e2 * r
        f1, f2 = f2, f1 + f2 * r
 
        a, b = f2 * x + e2, f2
        if a * a - n * b * b == 1:
            return a, b
lim = 1000
maior = (0,0)
for d in range(1,lim+1):
	if not math.sqrt(d).is_integer():
		s=solvePell(d)
		if s[0] > maior[0]:
			maior = s
			print(maior,d)
