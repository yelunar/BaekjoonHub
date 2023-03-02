N, K = map(int, input().split())
arr = [[0] * 7 for _ in range(2)]

for _ in range(N):
    a, b = map(int, input().split())
    arr[a][b] += 1

cnt = 0

for i in range(2):
    for j in range(7):
        if 0< arr[i][j] <= 2:
            cnt += 1
        elif arr[i][j] >= 3:
            cnt += arr[i][j] % 2 + 1

print(cnt)