import sys
input = sys.stdin.readline
# sys.stdin = open("input1.txt")
sys.setrecursionlimit(1000000)
"""
'최소일수', '주변의 토마토들을 익힘'  -> BFS
문제 속에 힌트가 있다
dfs를 쓰면 안되는 문제였다. 깊이 들어갈 일이 없기 때문
"""
from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


# bfs 특 queue 사용하기
# deque 모듈 안쓰면 시간복잡도 박살남(pop(0)이 시간복잡도가 O(n)이고 popleft()가 O(1)이라고 함)

def BFS():

    while queue:
        x, y = queue.popleft()
    
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny<M and arr[nx][ny] == 0: # 범위 조심해!
                arr[nx][ny] = arr[x][y] + 1 # 이렇게 하면 굳이 cnt안써도 되지
                queue.append([nx,ny])

    return

#########################################################

M,N = map(int, input().split()) # M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수
arr = [list(map(int, input().split())) for _ in range(N)]
queue = deque()
ans = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            queue.append([i, j])


BFS()

for i in arr:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)

    ans = max(ans, max(i))

print(ans-1)