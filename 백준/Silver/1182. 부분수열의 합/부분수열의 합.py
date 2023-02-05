# 조합 만들어서 더하기

from itertools import combinations

N, K = map(int, input().split()) 
numbers = list(map(int, input().split()))

cnt = 0

for i in range(1, N+1): #1부터 n까지
    com = combinations(numbers, i)

    for j in com:
        if sum(j) == K:
            cnt += 1
        
print(cnt)