import sys

n = int(sys.stdin.readline())
land = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

mini = 101
maxi = 0
for a in range(n):
    for b in range(n):
        if land[a][b] < mini:
            mini = land[a][b]
        if land[a][b] > maxi:
            maxi = land[a][b]

def safe(arr, num):
    global result
    temp = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] > num and visited[i][j] == 0:
                temp += 1
                queue = [i, j]
                visited[i][j] = 1
                while queue:
                    x = queue.pop(0)
                    y = queue.pop(0)
                    dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] > num and visited[nx][ny] == 0:
                            queue.append(nx)
                            queue.append(ny)
                            visited[nx][ny] = 1

    if temp > result:
        result = temp

if mini == maxi:
    print(1)
else:
    result = 0
    for num in range(mini, maxi):
        safe(land, num)

    print(result)