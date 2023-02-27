arr = []
for i in range(4):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

max_num = 0
for i in range(4):
    for j in range(4):
        if arr[i][j] >= max_num:
            max_num = arr[i][j]

paper = []
for i in range(max_num):
    tmp = [0] * max_num
    paper.append(tmp)

for k in range(4):
    for i in range(arr[k][0] , arr[k][2]):
        for j in range(arr[k][1] , arr[k][3]):
            paper[i][j] = 1

cnt = 0
for i in range(max_num):
    for j in range(max_num):
        if paper[i][j] == 1:
            cnt +=1

print(cnt)