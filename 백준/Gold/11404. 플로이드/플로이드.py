import sys
input = sys.stdin.readline
# sys.stdin = open("input1.txt")
# sys.setrecursionlimit(1000000)

"""
ANS => n개의 줄을 출력
 i번째 줄에 출력하는 j번째 숫자는 도시 i에서 j로 가는데 필요한 최소 비용
---------------------------------------------------------------------------

- 다익스트라: 한 지점에서 다른 모든 지점까지의 최단 경로를 계산하는 알고리즘
- 플로이드 워셜: 모든 지점에서 다른 모든 지점까지의 최단 경로를 계산하는 알고리즘

<플로이드–워셜>
다음과 같이 3중 반복문을 이용해 구현할 수 있다.

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            adj[a][b] = min(adj[a][b], adj[a][k] + adj[k][b])
"""

INF = int(1e9)
n = int(input()) # 도시개수
m = int(input()) # 버스개수
graph = [[INF] * (n+1) for _ in range(n+1)]
ans = 0

# 같은 지점 0처리
for i in range(1, n+1):
    graph[i][i] = 0

# 그래프 정보
for _ in range(m):
    a, b, c = map(int, input().split()) # 시작 도시 a, 도착 도시 b, 한 번 타는데 필요한 비용 c
    graph[a][b] = min(graph[a][b], c)

# 플로이드 워셜
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            graph[i][j] = 0

for i in range(1, n+1):
    print(*graph[i][1:])