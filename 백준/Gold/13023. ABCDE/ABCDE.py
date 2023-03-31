import sys
# sys.stdin = open('input2.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

"""

"""
def DFS(depth, idx):
    global flag

    if depth == 5:
        flag = 1
        return
    visited[idx] = True
    for i in friends[idx]:
        if not visited[i]:
            DFS(depth+1, i)
    visited[idx] = False

    return

##############################################################################
N, M = map(int, input().split()) # N: 사람수, M: 친구 관계 수
friends = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

flag = 0
visited = [False] * N
for i in range(N):
    if not visited[i]:
        DFS(1,i)
    if flag == 1:
        break

print(flag)