import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
arr = [list(map(int, input().split())) for _ in range(19)]

dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

black = 0
white = 0


for x in range(19):
    for y in range(19):
        if arr[x][y] != 0:
            now = arr[x][y]

            for k in range(4):
                cnt = 1
                nx = x + dx[k]
                ny = y + dy[k]

                while 0 <= nx < 19 and 0 <= ny < 19 and arr[nx][ny] == now:
                    cnt += 1

                    if cnt == 5:
                        if 0 <= x - dx[k] < 19 and 0 <= y - dy[k] < 19 and arr[x - dx[k]][y - dy[k]] == now:
                            break
                        if 0 <= nx + dx[k] < 19 and 0 <= ny + dy[k] < 19 and arr[nx + dx[k]][ny + dy[k]] == now:
                            break
                        
                        print(now)
                        print(x + 1, y + 1)
                        sys.exit(0)

                    nx += dx[k]
                    ny += dy[k]

print(0)  