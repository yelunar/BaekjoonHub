import sys
# sys.stdin = open('input3.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

"""
최소 -> BFS 와 관련
DFS는 재귀로 돌기 때문에 최소와 거리가 멀다

"""
 
dx = [-1, 1, 2, 2, 1, -1, -2, -2]
dy = [2, 2, 1, -1, -2, -2, -1, 1]

def BFS():
    queue = deque()
    queue.append((start_x, start_y))

    while queue:
        x, y = queue.popleft()

        if x == end_x and y == end_y:
            return arr[x][y] -1 

        for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<= nx < L and 0<= ny < L and arr[nx][ny] == 0:
                     arr[nx][ny] = arr[x][y] + 1
                     queue.append((nx, ny))


for tc in range(int(input())):
    L = int(input()) # 한 변의 길이
    start_x, start_y = map(int, input().rstrip().split())
    end_x, end_y = map(int, input().rstrip().split())
    arr = [[0]*L for _ in range(L)]
    arr[start_x][start_y] = 1
    print(BFS())