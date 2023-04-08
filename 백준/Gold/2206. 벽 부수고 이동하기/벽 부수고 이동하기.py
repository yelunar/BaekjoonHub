import sys
from collections import deque
"""
모든 작업을 한 번의 BFS 탐색을 통해 처리해야했기 때문에, 
최적의 벽을 '탐색'하는 것보다는 '기록'하는 방식이 필요
=> 3차원 배열을 사용하여 벽 부숨 유무 나타내어야함
"""

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(a, b, c):
    queue = deque()
    queue.append((a, b, c))

    while queue:
        x, y, z = queue.popleft()

        if x == n-1 and y == m-1:  # 끝 점에 도달하면 이동 횟수를 출력
            return visited[x][y][z]

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0<= nx < n and 0<= ny < m:
                # 다음 이동할 곳이 벽이 아니고, 아직 한 번도 방문하지 않은 곳이면
                if arr[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    queue.append((nx, ny, z))
                
                # 다음 이동할 곳이 벽이고, 벽 파괴 기회 있으면
                elif arr[nx][ny] == 1 and z == 0:
                    visited[nx][ny][1] = visited[x][y][z] + 1
                    queue.append((nx, ny, 1))
    return -1

# ------------------------------------------------------------------

n, m = map(int, input().split()) # N×M의 행렬
arr = [list(map(int, input())) for _ in range(n)]
visited =  [[[0] * 2 for _ in range(m)] for _ in range(n)] # 2차원 배열의 원소가 리스트이게 3차원 배열 만들기
visited[0][0][0] = 1

print(bfs(0, 0, 0))