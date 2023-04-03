"""
폭탄이 있는 칸은 3초가 지난 후에 폭발
폭탄이 폭발한 이후에는 폭탄이 있던 칸이 파괴되어 빈 칸, 인접한 네 칸도 함께 파괴
빈 칸은 '.'로, 폭탄은 'O'
"""
dy = [1,-1,0,0]
dx = [0,0,-1,1]

def DFS(depth, N):

    if depth == N:
        for i in arr:
            print(''.join(i))
        return
    
# ----------------------------------------

    lst = []

    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'O':
                lst.append([i, j]) # 폭탄있는 위치 저장

    for x, y in lst:
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0<= nx<R and 0<= ny <C and arr[nx][ny] == '.':
                arr[nx][ny] = 'O'
   

    for i in range(R):
        for j in range(C):
            if arr[i][j] == '.':
                arr[i][j] = 'O'
            else:
                arr[i][j] = '.'
    
    DFS(depth+1, N)

######################################################################

R, C, N = map(int, input().split()) # R×C인 직사각형 격자판 / 시간N만큼 조사
arr = [list(input()) for _ in range(R)]
bomb = [['O']*C for _ in range(R)]

if N % 2: 
    DFS(0, N//2)
else: # 폭탄 설치
    for i in bomb:
        print(''.join(i)) 