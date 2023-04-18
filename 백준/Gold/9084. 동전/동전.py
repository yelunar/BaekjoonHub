import sys
input = sys.stdin.readline
# sys.stdin = open('input3.txt')
sys.setrecursionlimit(10**6)

"""
 동전에는 1원, 5원, 10원, 50원, 100원, 500원
 동전의 종류가 주어질 때에 주어진 금액을 만드는 모든 방법을 세는 프로그램
"""

for _ in range(int(input())):
    n  = int(input()) # 동전 가지수
    coins = [0] + list(map(int, input().split()))
    m = int(input()) # 만들어야할 금액

    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = dp[i-1][j] # 전에 개수 물려받기
            if (j - coins[i]) >= 0:
                dp[i][j] += dp[i][j-coins[i]]
    
    print(dp[n][m])
