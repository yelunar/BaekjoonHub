import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10000)

"""
<청소년 상어>
(1) 상어는 물고기를 잡아먹고 진행 방향은 잡아먹은 물고기의 진행 방향
(2) 모든 물고기 이동
    물고기가 이동가능할 때까지 반시계 방향으로 45도씩 최대 한 바퀴 회전
    진행 방향에 상어없으면 해당 좌표로 1칸 이동
    이동할 곳에 물고기가 존재하면 해당 물고기와 위치 서로 교환(진행 방향은 변화없음)
(3) 잡아먹을 물고기 있는지 확인
    상어가 잡아먹을 물고기가 존재한다면 (1)로 돌아감
    상어가 잡아먹을 물고기가 더 이상 존재하지 않는다면 함수 리턴 물고기 먹는양 최댓값 출력
"""
import copy

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def dfs(now_x, now_y, cnt, arr):
    global max_ans

    # 최대값 반환
    cnt += arr[now_x][now_y][0]
    max_ans = max(max_ans, cnt)
    arr[now_x][now_y][0] = 0

    # (1) 물고기 움직이기
    for next in range(1, 17):
        next_x, next_y = -1, -1
        for x in range(4):
            for y in range(4):
                if arr[x][y][0] == next:
                    next_x, next_y = x, y
                    break
        if next_x == -1 and next_y == -1:
            continue
        dir = arr[next_x][next_y][1]

        for k in range(8):
            n_dir = (dir+k) % 8 # 방향 바꿔
            nx = next_x + dx[n_dir]
            ny = next_y + dy[n_dir]
            if not (0 <= nx < 4 and 0 <= ny < 4) or (nx == now_x and ny == now_y):
                continue
            arr[next_x][next_y][1] = n_dir
            arr[next_x][next_y], arr[nx][ny] = arr[nx][ny], arr[next_x][next_y]
            break

    # 상어가 먹기
    sharkd = arr[now_x][now_y][1]
    for i in range(1, 5):
        nx = now_x + dx[sharkd]*i
        ny = now_y + dy[sharkd]*i
        if (0<= nx < 4 and 0<= ny < 4) and arr[nx][ny][0] > 0:
            dfs(nx, ny, cnt, copy.deepcopy(arr))


###########################################################################

arr = [[] for _ in range(4)] # # 물고기 번호, 방향

for i in range(4):
    info = list(map(int, input().split()))
    tmp = []
    for j in range(4):
        # 물고기 번호, 방향
        tmp.append([info[2*j], info[2*j+1]-1])
    arr[i] = tmp

max_ans = 0

dfs(0, 0, 0, arr)
print(max_ans)