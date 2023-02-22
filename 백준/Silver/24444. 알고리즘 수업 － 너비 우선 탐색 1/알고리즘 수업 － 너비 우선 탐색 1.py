import sys
input = sys.stdin.readline
from collections import deque

N, M, start = map(int, input().split())
data = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 1

for _ in range(M):
    S, G = map(int, input().split())
    data[S].append(G)
    data[G].append(S) # 양방향 노드 설정   

def BFS(start):
    global cnt

    queue = deque([start])
    visited[start] = 1

    while queue:
        start = queue.popleft()
        data[start].sort()
        for next in data[start]:
            if visited[next] == 0:
                cnt += 1
                visited[next] = cnt
                queue.append(next)

BFS(start)

for i in visited[1:]:
    print(i)