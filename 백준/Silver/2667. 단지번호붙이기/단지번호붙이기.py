from collections import deque
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def BFS(x, y):
    queue=deque() # 빈 데크 설정
    queue.append((x, y))
    arr[x][y] = 0 # visited 해준 것과 같음
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if (0 <= nx < N and 0 <= ny < N) and arr[nx][ny] == 1:
                arr[nx][ny] = 0
                queue.append((nx, ny))
                cnt += 1
    return cnt



N = int(input()) # N*N
arr = [list(map(int, input())) for _ in range(N)]
visitied = [[0]*N for _ in range(N)] # 여기서는 안필요할 수도 있음

ans = [] # 오름차순으로 출력하되, len(ans) 먼저 출력하기
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            ans.append(BFS(i, j))

ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i])