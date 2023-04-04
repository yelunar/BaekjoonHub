import sys
# sys.stdin = open('input2.txt')
input = sys.stdin.readline

"""
<상어초등학교>
학생의 만족도를 구하려면 그 학생과 인접한 칸에 앉은 좋아하는 학생의 수
그 값이 0이면 학생의 만족도는 0, 1이면 1, 2이면 10, 3이면 100, 4이면 1000

원래 조건마다 함수 만들어주려고 했는데 ,,, 
"""
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N = int(input())
friends = [list(map(int, input().split())) for _ in range(N**2)]
arr = [[0]*N for _ in range(N)] # 애들 앉힐 0으로 채워진 리스트

## 학생 수 만큼 for문을 돌며 자리에 앉혀 줌.
for i in range(N**2):
    friend = friends[i] # 애 한명의 정보

    tlst = []
    for x in range(N):
        for y in range(N):
            if arr[x][y] == 0:
                like, blank = 0, 0
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0<= nx < N and 0<= ny < N:
                        if arr[nx][ny] in friend[1:]: # 좋아하는 애들이 있는지 확인
                            like += 1
                        if arr[nx][ny] == 0:
                            blank += 1
                tlst.append([like, blank, x, y])

    # like와 blank는 값이 클수록, 행이랑 열의 번호는 작을수록 우선순위가 높으니까 그게 맞게 정렬
    tlst.sort(key = lambda x:(-x[0], -x[1], x[2], x[3])) # 마이너스 붙어있으면 내림차순으로 정렬
    arr[tlst[0][2]][tlst[0][3]] = friend[0] # 정렬하고 제일 우선순위 높은 행, 열 번호로 앉힘

ans = 0
friends. sort() #점수매길때는 순서대로 주기위해 정렬

for x in range(N):
    for y in range(N):
        cnt = 0
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] in friends[arr[x][y]-1]:
                    cnt += 1
        if cnt != 0:
            ans += 10**(cnt-1)
print(ans)