import sys
input = sys.stdin.readline
# sys.stdin = open('input3.txt')
# sys.setrecursionlimit(10**6)
# 
"""
2^N × 2^N인 격자로 나누어진 얼음판 / (r, c)에 있는 얼음의 양

 ANS
 남아있는 얼음 A[r][c]의 합
 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수
"""
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

n, q = map(int, input().split()) 
arr = [list(map(int, input().split())) for _ in range(2**n)]
L_list = list(map(int, input().split())) # 1 -> 2**L

for L in L_list: # q번 시전
    # (1)  2^L × 2^L 크기의 부분 격자로 나눈다.
    new_arr = [[0] *(2**n) for _ in range(2**n)]
    
    # (2) 모든 부분 격자를 시계 방향으로 90도 회전
    for i in range(0, 2**n, 2**L): 
        for j in range(0, 2**n, 2**L):
            for a in range(2**L):
                for b in range(2**L):
                    new_arr[i+b][j+2**L-a-1] = arr[i+a][j+b]

    arr = [[0] *(2**n) for _ in range(2**n)]
    # (3) 얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않은 칸은 얼음의 양이 1 줄어듦
    for x in range(2**n):
        for y in range(2**n):
            cnt = 0
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0<= nx < 2**n and 0<= ny < 2**n and new_arr[nx][ny]:
                        cnt += 1
            if new_arr[x][y]:
                if cnt < 3:
                    arr[x][y] = new_arr[x][y] - 1
                else:
                    arr[x][y] = new_arr[x][y]

# 덩어리 계산
ice_sum = 0
ice_list = [0]
visited = [[0] *(2**n) for _ in range(2**n)]
for x in range(2**n):
    for y in range(2**n):
        tmp = []
        if arr[x][y] and not visited[x][y]:
            tmp.append([x, y])
            visited[x][y] = 1
            ice_sum += arr[x][y]
            cnt = 1
            while tmp:
                ax, ay = tmp.pop()
                for k in range(4):
                    nx, ny = ax + dx[k], ay + dy[k]
                    if 0<= nx < 2**n and 0<= ny < 2**n and not visited[nx][ny] and arr[nx][ny]:
                        tmp.append([nx, ny])
                        visited[nx][ny] = 1
                        ice_sum += arr[nx][ny]
                        cnt += 1
            ice_list.append(cnt)
    
print(ice_sum)
print(max(ice_list))
                        