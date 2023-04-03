import sys
input = sys.stdin.readline
# sys.stdin = open("input1.txt")
sys.setrecursionlimit(1000000)
"""
'최소일수', '주변의 토마토들을 익힘'  -> BFS
정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸

3차원배열에서 델타는 그냥 두개만 더 추가해주면 됨
"""

from collections import deque

dz = [0, 0, 0, 0, 1, -1]
dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]

def BFS():
    
    while queue:
        z, x, y = queue.popleft()

        for k in range(6):
            nx = x + dx[k]
            ny = y + dy[k]
            nz = z + dz[k]

            if 0<=nx<N and 0<=ny<M and 0<=nz<H and arr[nz][nx][ny] == 0:
                arr[nz][nx][ny] = arr[z][x][y] + 1
                queue.append([nz, nx, ny])
    return

#############################################################################

M, N, H = map(int ,input().split())  # M가로 , N세로, H 높이
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
queue = deque([])
ans = 0

for k in range(H):
    for i in range(N):
        for j in range(M):
            if arr[k][i][j] == 1:
                # print(arr[k][i][j])
                queue.append([k,i,j])

BFS()

for large in arr:
    for small in large:
        for i in small:
            if i == 0:
                print(-1)
                exit(0)
    
        ans = max(ans, max(small))
    
print(ans-1)

"""
[[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 
[[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]]

"""