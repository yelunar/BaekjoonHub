import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
"""
공기청정기는 항상 1번 열에 설치, 크기는 두 행을 차지
(1) 네방향으로 미세먼지 확산, 확산되는 양은 Ar,c//5 이고 확산되는 양은 빼줘야함
(2) 공기청정기 작동 -> 위쪽 공기청정기의 바람은 반시계방향으로 순환, 아래쪽 공기청정기의 바람은 시계방향으로 순환
    바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동
    공기청정기로 들어간 미세먼지는 모두 정화

T초가 지난 후 구사과의 방에 남아있는 미세먼지의 양?
"""
    
def dust():
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    lst = [[0]*C for _ in range(R)]

    for x in range(R):
        for y in range(C):
            cnt = 0

            if arr[x][y] == 0:
                continue

            if arr[x][y] == -1: # 공기청정기 찍어주고
                lst[x][y] = -1
                continue
            
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0<= nx < R and 0<= ny < C and arr[nx][ny]!=-1:
                    cnt += 1
                    lst[nx][ny] += arr[x][y] //5
            
            lst[x][y] += (arr[x][y] - (arr[x][y] //5) * cnt)
    
    for i in range(R):
        for j in range(C):
            arr[i][j] = lst[i][j]
#---------------------------------------------------------------------------

def air_up():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    now, dir = 0, 0
    x, y = stack[0], 1
    while True:
        nx = x + dx[dir]
        ny = y + dy[dir]
        if x == stack[0] and y == 0:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            dir += 1
            continue
        arr[x][y], now = now, arr[x][y]
        x, y = nx, ny

def air_down():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    now, dir = 0, 0
    x, y = stack[1], 1
    while True:
        nx = x + dx[dir]
        ny = y + dy[dir]
        if x == stack[1] and y == 0:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            dir += 1
            continue

        arr[x][y], now = now, arr[x][y]
        x, y = nx, ny

###########################################################################

R, C, T = map(int, input().split()) 
arr = [list(map(int, input().split())) for _ in range(R)]
stack = [] # [[2, 0], [3, 0]]

for i in range(R):
    if arr[i][0] == -1:
        stack.append(i) # 공기청정기 위치 넣어줌
    if len(stack) == 2:
        break
      
for _ in range(T):
    dust()
    air_up()
    air_down()

#############################################################################
ans = 0

for i in range(R):
    for j in range(C):
        if arr[i][j] > 0:
            ans += arr[i][j]

print(ans)
