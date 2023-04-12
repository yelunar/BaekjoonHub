import sys
input = sys.stdin.readline
# sys.stdin = open("input1.txt")
# sys.setrecursionlimit(1000000)


"""
<플로이드2>
 - 최단 거리를 갱신할 때, 경로 배열에 해당 정점에 거쳐온 경유지를 기록
 - 플로이드가 끝난 후, 경로 배열에 적힌 수대로 역추적하며 거슬러 올라가면 됨
"""

INF = int(1e9)
n = int(input()) # 도시개수
m = int(input()) # 버스개수
graph = [[INF] * (n+1) for _ in range(n+1)] # 최소비용 반환
trace = [[()] * (n+1) for _ in range(n+1)] # 최단 경로 반환

# 같은 지점 0처리
for i in range(1, n+1):
    graph[i][i] = 0

# 그래프 정보
for _ in range(m):
    a, b, c = map(int, input().split()) # 시작 도시 a, 도착 도시 b, 한 번 타는데 필요한 비용 c
    graph[a][b] = min(graph[a][b], c)
    trace[a][b] = (a, b)

# 플로이드 워셜
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            cost = graph[i][k] + graph[k][j]
            if graph[i][j] > cost:
                graph[i][j] = cost
                trace[i][j] = trace[i][k] + trace[k][j][1:]

for i in range(1, n+1):
    tmp = []
    for j in range(1, n+1):
        if graph[i][j] == INF:
            tmp.append(0) # 갈 수 없을 때 0 반환
        else:
            tmp.append(graph[i][j])
    print(*tmp)

for i in range(1, n+1):
    for j in range(1, n+1):
        print(len(trace[i][j]), *trace[i][j])