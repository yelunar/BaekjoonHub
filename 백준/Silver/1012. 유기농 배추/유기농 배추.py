dx = [0, 0, 1, -1] # 방향 델타
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue=[(x, y)]
    arr[x][y] = 0

    while queue:
        x, y = queue.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if (0 <= nx < N and 0 <= ny < M) and arr[nx][ny] == 1:
                arr[nx][ny] = 0
                queue.append((nx, ny))
    return


T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split()) #가로 세로 배추위치개수
    arr = [[0]*M for _ in range(N)]
    cnt = 0 # 벌레개수

    for _ in range(K):
        a, b = map(int, input().split())
        arr[a][b] = 1
            
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
            # 배추 있는 곳 만나면 함수 실행에서 인접한 배추 다 0으로 바꿈    
                bfs(i, j) 
                cnt += 1
    
    print(cnt)