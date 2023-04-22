import sys
input = sys.stdin.readline
# sys.stdin = open('input3.txt')
sys.setrecursionlimit(10**6)

"""
세준이는 M개의 가방을 가지고 있고 각각의 가방은 C그램의 보석을 담을 수 있다.
ans =>  세준이가 가져갈 수 있는 최대 보석의 개수

now: 지금 가방 용량 남은 만큼
idx: 가방 위치
5 2 5
2 2 2 2 2
"""

n, m, c = map(int, input().split()) # 보석의 개수 N, 가방의 개수 M, 가방의 최대 한도 C
jewel = list(map(int, input().split()))
dp = [[[0 for _ in range(c+1)] for _ in range(m+1)] for _ in range(1<<14)]


def theif(thing, idx, now):
    if thing == ((1<<n)-1) or idx >= m: # 보석 다 썼으면
        return 0
    if dp[thing][idx][now] != 0: # 가방 다썼으면
        return dp[thing][idx][now]
    
    ans = 0
    
    for i in range(n): # 보석 하나씩 넣어본다
        if (thing & (1<<i) ) != 0 or jewel[i] > c: # 이미 사용한 보석이면 건너뜀
            continue
        if now >= jewel[i]: # 가방에 넣을 수 있으면
            ans = max(ans, theif(thing | (1<<i), idx, now-jewel[i])+1)
        else: # 못넣으면 다음 다방으로
            ans = max(ans, theif(thing, idx+1, c))
        
    dp[thing][idx][now] = ans
    return ans

print(theif(0, 0, c))

