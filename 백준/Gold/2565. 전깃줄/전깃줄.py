import sys 
# sys.stdin = open('input1.txt')
input = sys.stdin.readline

"""
ans =>
모든 전깃줄이 서로 교차하지 않게 하기 위해 없애야 하는 전깃줄의 최소 개수

가긴분수
"""

n = int(input()) # 두 전봇대 사이 전깃줄개수
dp = [1 for _ in range(n)] 
arr = sorted([list(map(int, input().split())) for _ in range(n)] )

for i in range(n):
    for j in range(i):
        if arr[i][1] > arr[j][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))