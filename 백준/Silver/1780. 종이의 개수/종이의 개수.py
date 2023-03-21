import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

"""
  N*N크기의 행렬로 표현되는 종이
 -1로만 채워진 종이의 개수, 0으로만 채워진 종이의 개수, 1로만 채워진 종이의 개수 출력

 DFS쓰는건 알거같음 처음에 9->3->1로 진행


"""
def DFS(x, y, size):
    global cnt_minus, cnt_zero, cnt_one
    now = arr[x][y]

    for i in range(x, x+size):
        for j in range(y, y+size):
            if arr[i][j] != now:
                for k in range(3):
                    for l in range(3):
                        DFS(x+k*size//3, y+l*size//3, size//3)
                return
    if now == -1:
        cnt_minus += 1
    elif now == 0:
        cnt_zero += 1
    else:
        cnt_one += 1

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

cnt_minus = 0
cnt_zero = 0
cnt_one = 0

DFS(0,0,N)
print(cnt_minus)
print(cnt_zero)
print(cnt_one)