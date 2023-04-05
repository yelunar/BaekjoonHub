import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

"""
<비바라기>
(r, c)는 격자의 r행 c열에 있는 바구니를 의미하고, 
A[r][c]는 (r, c)에 있는 바구니에 저장되어 있는 물의 양

-격차 1,1 부터 시작
- N -> 1로 행, 열 연결됨
- 좌우 2만큼 구름 생김

(N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름
 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전
"""

# from collections import deque

N, M = map(int,input().split()) # 구름 이동을 M번 -> 8 방향
arr = [list(map(int,input().split())) for _ in range(N)]
move = [] # 이동의 정보 di 방향으로 si칸 이동

for i in range(M):
    tmp = list(map(int,input().split()))
    move.append([tmp[0]-1, tmp[1]])

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

# ------------------------------------------------------------------------

clouds =[[N-1,0], [N-1,1], [N-2,0], [N-2,1]]

for i in range(M):

    dir, distance = move[i]
    next = []

    for cloud in clouds:
        nx = (cloud[0] + dx[dir] * distance) % N
        ny = (cloud[1] + dy[dir]* distance) % N
        next.append([nx,ny])
   
    visited = [[0]*N for _ in range(N)]
    for cloud in next:
        
        arr[cloud[0]][cloud[1]] += 1 # 비 1씩 뿌리기
        visited[cloud[0]][cloud[1]] = 1

    clouds = [] # 구름 모두 소멸


    di = [-1, -1, 1, 1] # 인접 대각선 조사
    dj = [1, -1, 1, -1]

    for i, j in next:
        cnt = 0

        for k in range(4):
            ni = i+ di[k]
            nj = j+ dj[k]

            if 0<= ni <N and 0<= nj <N and arr[ni][nj]: # 물이 있을 때
                cnt += 1
        arr[i][j] += cnt

    # 4. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2 and visited[i][j] == 0:
                arr[i][j] -= 2
                clouds.append([i,j])
total = 0
for i in range(N):
    total += sum(arr[i])
print(total)
