import sys
input = sys.stdin.readline
# sys.stdin = open('input2.txt')
# sys.setrecursionlimit(10**6)
# 
"""

"""
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def new_smell():
    for i in range(n):
        for j in range(n):
            if smell[i][j][1] > 0: # 냄새 남아있으면
                smell[i][j][1] -= 1
            # 거기에 상어 있으면
            if arr[i][j] != 0:
                smell[i][j] = [arr[i][j], k]

def move():
    new_arr = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if arr[x][y] != 0:
                direction = direc[arr[x][y] - 1]
                flag = False

                for idx in prior[arr[x][y] - 1][direction -1]:
                    nx = x + dx[idx-1]
                    ny = y + dy[idx-1]
                    if 0<= nx < n and 0<= ny < n:
                        if smell[nx][ny][1] == 0: # 냄새 없는 곳 발견
                            direc[arr[x][y] - 1] = idx
                            # t상어이동
                            if new_arr[nx][ny] == 0:
                                new_arr[nx][ny] = arr[x][y]
                            else:
                                new_arr[nx][ny] = min(arr[x][y], new_arr[nx][ny])
                            flag = True
                            break
                if flag:
                    continue

                # 빈 냄새 없으면 자기 냄새 있는 곳으로 ㄱㄱ
                for idx in prior[arr[x][y] - 1][direction -1]:
                    nx = x + dx[idx-1]
                    ny = y + dy[idx-1]
                    if 0<= nx < n and 0<= ny < n:
                        if smell[nx][ny][0] == arr[x][y]: # 자기 냄새 발견
                            direc[arr[x][y] - 1] = idx
                            new_arr[nx][ny] = arr[x][y]
                            break
    return new_arr


#----------------------------------------------------------------

n, m, k = map(int, input().split())

# 초기 상어 위치
arr = [list(map(int, input().split())) for _ in range(n)]

shark = [[0, 0] for _ in range(m)]

# 상어 초기 방향
direc = list(map(int, input().split()))

# 상어 방향 우선순위 위 아래 왼 오
prior = []
for _ in range(m):
    tmp = []
    for _ in range(4):
        tmp.append(list(map(int, input().split())))
    prior.append(tmp)

# 냄새 정보 입력 / 번호, 시간, 방향
smell = [[[0, 0]] * n for _ in range(n)]

ans = 0

while True:
    new_smell()
    new_info = move()
    arr = new_info
    ans += 1

    flag = False

    for i in range(n):
        for j in range(n):
            if arr[i][j] > 1:
                flag = True
    
    if not flag:
        print(ans)
        break
    if ans >= 1000:
        print(-1)
        break