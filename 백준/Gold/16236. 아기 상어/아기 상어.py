import sys
# sys.stdin = open('input2.txt')
input = sys.stdin.readline

"""
가까운 먹이를 찾는 탐색 문제이기 때문에 BFS
BFS를 사용할 시 입력으로는 현재 아기 상어의 위치를 생각할 수 있고, 
출력으로는 후보를 리스트를 반환
후보 리스트는 우선 순위가 있기 때문에 정렬 사용
"""

from collections import  deque

dx = [0, 0, -1, 1] # 상하좌우로 이동
dy = [-1, 1, 0, 0]

def bfs(i, j):
    visited = [[0]*N for _ in range(N)]
    queue = deque()
    queue.append([i, j])
    visited[i][j] = 1
    lst = [] # 우선순위 때문에 그거 반영할 빈 리스트가 있어야해

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0<= nx<N and 0<= ny < N and not visited[nx][ny]:
                if 0< arr[nx][ny] < size[0]: # 상어보다 크기 작으면 (0보다 클때 조건을 넣어줘야해..... )
                    visited[nx][ny] = visited[x][y] + 1
                    lst.append([visited[nx][ny]-1, nx, ny]) # 우선순위 고려 리스트에 넣어줌

                elif arr[nx][ny] == size[0]: # 상어랑 물고기랑 크기 같으면
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx, ny]) # 그냥 다음 경로 가는거만 반영

                elif not arr[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx, ny]) # 그냥 다음 경로 가는거만 반영

    # 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기,
    # 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
    # return sorted(lst, key = lambda x: ([-x[2], -x[0], -x[1]]))  # 거리 x좌표 y좌표 순으로 정렬
    return sorted(lst, key=lambda i: [i[0], i[1], i[2]])
"""
lst
[[0, 2, 3], 
[0, 2, 1], 
[0, 1, 2], 
[0, 3, 2]]
"""

##############################################################################

N = int(input()) # 공간크기
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            x, y = i, j
            # bfs(i, j)

# --------------------------------------------------------

size = [2, 0]
cnt = 0
# 8. 맨 앞의 후보만 먹고 위치 이동후 다시 BFS 해야한다
while True:
    arr[x][y] = 0
    cand = deque(bfs(x, y))

    if not cand:
        break

    # 7. 후보리스트가 나오면 맨 앞의 후보 먹이를 뽑아 그 위치로 이동한다.
    step, xx, yy = cand.popleft()
    cnt += step
    size[1] += 1

    # 9. 몇 개를 먹었는지 몇 초간 이동했는지 체크해 줄 필요가 있다.
    if size[0] == size[1]:
        size[0] += 1
        size[1] = 0

    x, y = xx, yy

print(cnt)