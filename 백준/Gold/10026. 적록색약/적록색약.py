import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10000)

"""

"""

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def DFS(x, y, visited):
    
    stack = [(x, y)]
    visited[x][y] = True
    
    while stack:
        x, y = stack.pop()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and arr[x][y] == arr[nx][ny]:
                visited[nx][ny] = 1
                stack.append((nx,ny))


N = int(input())
arr = [list(input()) for _ in range(N)]
visited_normal = [[False]*N for _ in range(N)]
visited_green = [[False]*N for _ in range(N)]

cnt_normal, cnt_green = 0, 0


for i in range(N):
    for j in range(N):
        if not visited_normal[i][j]:
            DFS(i, j, visited_normal)
            cnt_normal += 1

for i in range(N):
    for j in range(N):
        if arr[i][j] == "R":
            arr[i][j] = "G"

for i in range(N):
    for j in range(N):
        if not visited_green[i][j]:
            DFS(i, j, visited_green)
            cnt_green += 1

print(cnt_normal, cnt_green)