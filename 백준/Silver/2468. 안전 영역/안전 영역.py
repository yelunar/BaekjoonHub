import sys
sys.setrecursionlimit(100000)

# sys.stdin = open('input.txt')

def dfs(x, y, number):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<= nx < n and 0<= ny < n and visited[nx][ny] == 0:
            if arr[nx][ny] > number:
                visited[nx][ny] = 1
                dfs(nx, ny, number)

n = int(input())
arr = []
max_num = 0
ans = 1

dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

    for j in tmp:
        if j > max_num:
            max_num = j

for i in range(max_num):
    visited = [[0]*n for _ in range(n)]
    cnt = 0

    for j in range(n):
        for k in range(n):
            if arr[j][k] > i and visited[j][k] == 0:
                cnt += 1
                visited[j][k] = 1
                dfs(j, k, i)
    
    ans = max(ans, cnt)
print(ans)