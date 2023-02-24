N = int(input()) # 수열의 길이
data = list(map(int, input().split()))

length = []

# 올라가는거 조사
cnt = 1
for i in range(1, N):
    if data[i] >= data[i-1]:
        cnt += 1
    else:
        length.append(cnt)
        cnt = 1
length.append(cnt)

cnt = 1       
for i in range(1, N):
    if data[i] <= data[i-1]:
        cnt += 1
    else:
        length.append(cnt)
        cnt = 1
length.append(cnt)

print(max(length))