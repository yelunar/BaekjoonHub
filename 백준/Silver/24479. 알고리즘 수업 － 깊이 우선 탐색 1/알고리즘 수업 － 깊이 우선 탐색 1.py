import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N, M, start = map(int, input().split())
data = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 1

for _ in range(M):
    S, G = map(int, input().split())
    data[S].append(G)
    data[G].append(S) # 양방향 노드 설정   

def DFS(start):
    global cnt
    visited[start] = cnt
    data[start].sort()

    for next in data[start]:
        if not visited[next]:
            cnt += 1
            DFS(next)

DFS(start)

for i in visited[1:]:
    print(i)