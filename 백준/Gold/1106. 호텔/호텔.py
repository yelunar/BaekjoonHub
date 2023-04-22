import sys
input = sys.stdin.readline
# sys.stdin = open('input3.txt')
sys.setrecursionlimit(10**6)

"""
인덱스를 확보해야 하는 고객 수로 하고, 
그 고객을 확보하는 데 사용되는 최소 비용을 값으로 하는 dp 리스트 만들기
"""
INF = int(1e9)
c, n = map(int, input().split()) # c명 늘리기 위해 홍보할수 있는 도시개수n
info = [list(map(int, input().split())) for _ in range(n)] # 비용, 고객수
dp = [INF for _ in range(c+100)] # 고객수 최대 100명
dp[0] = 0 # 0명일땐 0원

for cost, people in info:
    for i in range(people, c+100):
        dp[i] = min(dp[i - people]+cost , dp[i])

print(min(dp[c:]))
