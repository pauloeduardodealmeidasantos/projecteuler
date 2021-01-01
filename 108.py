def solve(n): 
    ans = 0
    y = n + 1
    while(y <= n * n + n): 
        if ((n * n) % (y - n) == 0): 
            ans += 1
        y += 1
    return ans 
n = 4
while solve(n) <= 1000:
	n+=1
	print(n)
print(n)
