arr = [[''] * 1003 for i in range(1003)] # 도화지
N = int(input()) # 색종이 장수
for k in range(N):
    x, y, width, height = map(int, input().split())
    for i in range(y, y+height):
        for j in range(x, x+width):
            arr[i][j] = str(k)
result = []
cnt = 0
for k in range(N):
    for i in range(1001):
        for j in range(1001):
            if arr[i][j] == str(k):
                cnt += 1
    result.append(cnt)
    cnt = 0

for i in range(len(result)):
    print(result[i])