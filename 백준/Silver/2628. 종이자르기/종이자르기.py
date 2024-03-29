# 가로와 세로의 길이는 최대 100㎝
# 가로로 자르는 점선은 0과 점선 번호가 차례로 주어지고, 
# 세로로 자르는 점선은 1과 점선 번호

# 가장 큰 종이 조각의 넓이

garo, sero = map(int, input().split()) # 10 8
N = int(input()) # 칼로 잘라야하는 점선의 개수

paper = [[0, garo],[0, sero]]

for i in range(N):
    a, b = map(int, input().split())
    if a == 0:
        paper[1].append(b)
    else:
        paper[0].append(b)

paper[0].sort(reverse=False)
paper[1].sort(reverse=False)


tmp = []
for i in range(1, len(paper[0])):
    tmp.append(abs(paper[0][i] - paper[0][i-1]))
real_garo = max(tmp)

tmp = []
for i in range(1, len(paper[1])):
    tmp.append(abs(paper[1][i] - paper[1][i-1]))
real_sero = max(tmp)

print(real_sero*real_garo)
