#리트~루트까지 거리 총 합-> 홀수면 YES 짝수면 NO

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(v):

    visited[v] = True # 방문 처리
    for i in arr[v]:
        if not visited[i]:
            distance[i] = distance[v] + 1
            dfs(i)

    return 

# 선: 성원 형석
N = int(input()) # 트리 정점 개수
arr = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [False] * (N+1)
distance = [0 for _ in range(N+1)]

dfs(1)

ans = 0
for i in range(2, N+1):
    if len(arr[i]) == 1:
        ans += distance[i]

if ans % 2 == 0:
    print("No")
else:
    print("Yes")