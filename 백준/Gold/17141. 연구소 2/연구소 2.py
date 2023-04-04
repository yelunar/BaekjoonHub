import sys
# sys.stdin = open('input2.txt')
from collections import deque
input = sys.stdin.readline
from itertools import combinations
"""
<연구소2>
0은 빈 칸, 1은 벽, 2는 바이러스를 놓을 수 있는 칸

"""

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def BFS(comb):
    queue = deque(comb)
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    cnt = 0 # 최솟값 찾기 위한 변수

    for x, y in queue:
        visited[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0<= nx < N and 0<= ny < N:
                if visited[nx][ny] == -1 and arr[nx][ny] != 1:
                    queue.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1
                    cnt = max(cnt, visited[x][y] + 1) # 최소 횟수로 갱신

    # BFS 다 끝나고 빈칸있으면 inf 리턴, 나머지처리는 밑에서.. 
    for i in range(N):
        for j in range(N):
            if visited[i][j] == -1 and arr[i][j] != 1:
                return 1e9
    return cnt
    
#--------------------------------------------------------------------------

N, M = map(int, input().split()) # 연구소 크기N 바이러스개수M
arr = [list(map(int, input().split())) for _ in range(N)]
virus = []
ans = 1e9  # 최솟값 찾기 위해 초기값 설정

for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            virus.append([i,j])

for comb in combinations(virus, M): # 바이러스 좌표 중 M개를 뽑은 모든 경우에 대해서 bfs 수행하며 최솟값 갱신
    ans = min(BFS(comb), ans)

if ans == 1e9:
    print(-1)
else:
    print(ans)


"""
['v', 0, 0, 0, '-', '-', 0], 
[0, 0, '-', 0, '-', 'v', 0], 
[0, '-', '-', 0, '-', 0, 0], 
[0, '-', 0, 0, 0, 0, 0], 
[0, 0, 0, 'v', 0, '-', '-'],
[0, '-', 0, 0, 0, 0, 0]
['v', '-', 0, 0, 0, 0, 'v']
"""