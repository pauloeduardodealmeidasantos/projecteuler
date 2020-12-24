lst = list(range(1,101))
sum_sq = sum(map(lambda x: x*x, lst))
sum_sq_2 = sum(lst)**2
print(sum_sq_2-sum_sq)