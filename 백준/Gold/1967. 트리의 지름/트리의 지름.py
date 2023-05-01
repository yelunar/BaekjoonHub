import sys
# sys.stdin = open('input2.txt')
input = sys.stdin.readline
sys.setrecursionlimit(100000)

"""
<트리의 지름>
1. 아무 점이나 잡고(루트), 이 점에서 가장 거리가 먼 점 t를 잡는다.

2. t에서 가장 거리가 먼 점 u을 찾는다.

3. t - u가 트리의 지름. 끗

"""

n = int(input()) # 노드 개수
tree = [[] for _ in range(n+1)] # 앞에가 자식노드 / 뒤에가 가중치

for _ in range(n-1):
    parent, child, num = map(int, input().split())
    tree[parent].append((child, num)) # 양방향
    tree[child].append((parent, num))

visited = [-1] * (n+1)
visited[1] = 0 # 아무데나 시작해줌

def DFS(node, cost):
    for child, num in tree[node]:
        if visited[child] == -1: # 방문안했으면 방문한다
            visited[child] = num + cost
            DFS(child, num + cost)

DFS(1, 0)

v = visited.index(max(visited))
visited = [-1] * (n+1)
visited[v] = 0
DFS(v, 0)

print(max(visited))
