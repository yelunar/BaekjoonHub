N = int(input())
arr = [[0]*101 for _ in range(101)] #인덱스 조금더 더해줌

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] = 1

cnt = 0                 # 사각형 위에서부터 밑으로 내려가며 다음 항목이랑 숫자다른거 세기
for i in range(100):
    tmp = 0
    for j in range(100):
        if arr[j][i] != arr[j+1][i]:
            tmp += 1
    cnt += tmp

for i in range(100):  # 사각형 왼쪽에서 오른쪽으로가며 다음 항목 숫자다르면 세기
    tmp = 0
    for j in range(100):
        if arr[i][j] != arr[i][j+1]:
            tmp += 1
    cnt += tmp
# print(arr)
print(cnt)