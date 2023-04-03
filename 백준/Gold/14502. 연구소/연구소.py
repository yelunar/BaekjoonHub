import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10000)

"""
<연구소>
새로 세울 수 있는 벽의 개수는 무조건 3개
0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳
바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다
"""

from collections import deque
import copy

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def BFS():
    global ans

    copy_arr = copy.deepcopy(arr)
    queue = deque()

    for i in range(N):
        for j in range(M):
            if copy_arr[i][j] == 2:
                queue.append((i,j))

    while queue:
        
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0<= nx < N and 0<= ny < M:
                if copy_arr[nx][ny] == 0:
                    copy_arr[nx][ny] = 2
                    queue.append((nx, ny))

    result = 0
    for i in range(N):
        for j in range(M):
            if copy_arr[i][j] == 0:
                result += 1

    ans = max(ans, result)

#####################################################################

def makewalls(cnt):
    if cnt == 3:
        BFS()
        return
    
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                makewalls(cnt+1)
                arr[i][j] = 0

#######################################################################

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0

makewalls(0)        
print(ans)