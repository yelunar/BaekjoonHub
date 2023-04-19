import sys
input = sys.stdin.readline
# sys.stdin = open('input3.txt')
sys.setrecursionlimit(10**6)

"""
 ans => 경로표 출력

"""
INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)] # 집하장 정보
ans = [[0] * (n+1) for _ in range(n+1)] # 간선 정보

# 같은 지점 0, 무한처리
for i in range(1, n+1):
    graph[i][i] = 0
    ans[i][i] = INF

# 그래프 정보
for _ in range(m):
    a, b, c = map(int, input().split()) # 시작 도시 a, 도착 도시 b, 그 사이를 오가는데 필요한 시간 c
    graph[a][b] = c
    graph[b][a] = c
    ans[a][b] = b # a 출발 -> b 도착이면 b가 도착지점
    ans[b][a] = a

# 플로이드 워셜
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                ans[i][j] = ans[i][k]

for i in range(1, n+1):
    for j in range(1, n+1):
        if ans[i][j] == INF:
            ans[i][j] = '-'

for a in ans[1:]:
    print(*a[1:])