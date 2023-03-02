# 색종이 가로세로 10
N = int(input()) # 색종이 수
arr = [[0]*101 for _ in range(101)]
cnt = 0

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(y, y+10):
        for j in range(x, x+10):
            if arr[i][j] == 0:
                arr[i][j] = 1
                cnt += 1

print(cnt)