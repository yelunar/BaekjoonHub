dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y):
    cnt = 0
    q = [(x, y)]

    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
                q.append((nx, ny))
                arr[nx][ny] = arr[x][y] + 1                    

    return arr[N-1][M-1]

N, M = map(int, input().split())
arr = [] # 미로 다 넣음

for _ in range(N):
    tmp = list(map(int, input()))
    arr.append(tmp)

print(BFS(0,0))