import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

C, R = map(int, input().split()) # 가로, 세로
K = int(input()) # 대기번호

arr = [[0]*R for _ in range(C)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir = 0 # 방향
queue = [[0,0]]
arr[0][0] = 1

while queue:
    x, y = queue.pop()
    if arr[x][y] == K:
        print(x+1, y+1)
        exit()
    nx = x + dx[dir]
    ny = y + dy[dir]
    if 0 <= nx < C and 0 <= ny < R and not arr[nx][ny]:
        arr[nx][ny] = arr[x][y] + 1
        queue.append([nx,ny])
    else:
        dir = (dir+1) % 4
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0 <= nx < C and 0 <= ny < R and not arr[nx][ny]:
            arr[nx][ny] = arr[x][y] + 1
            queue.append([nx,ny])          

print(0)