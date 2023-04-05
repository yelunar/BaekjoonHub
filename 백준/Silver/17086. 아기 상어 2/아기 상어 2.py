import sys
input = sys.stdin.readline
# sys.stdin = open("input1.txt")
sys.setrecursionlimit(1000000)

"""
<아기상어2>
0은 빈 칸, 1은 아기 상어가 있는 칸
"""
from collections import deque

dx = [-1, -1, -1, 0, 1, 0, 1, 1]
dy = [-1, 0, 1, 1, 1, -1, 0, -1]


def bfs():

    while queue:
        x, y = queue.popleft()

        for k in range(8):
            nx, ny = x + dx[k], y + dy[k]

            if 0<= nx < N and 0<= ny < M: 
                if arr[nx][ny] == 0:
                    arr[nx][ny] = arr[x][y] + 1
                    queue.append((nx, ny))  # 새로운 지점의 좌표를 큐에 삽입
 
##################################################################

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
queue = deque()

for i in range(N):
    for j in range(M):
        if arr[i][j]: # 상어가 있는 위치에서 탐색하기 위해 
            queue.append((i, j))

bfs()

print(max(map(max, arr))-1)   
# print(max(max(arr))-1)         