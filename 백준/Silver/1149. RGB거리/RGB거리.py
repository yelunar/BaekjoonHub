import sys
# sys.stdin = open('input2.txt')
# input = sys.stdin.readline

"""
집을 빨강, 초록, 파랑으로 칠하는 비용
앞 뒤 집 색깔 다름

ANS =>  모든 집을 칠하는 비용의 최솟값을 출력
"""

n = int(input()) # 집의 수

colors = [] # 각 리스트 별로 빨강, 초록, 파랑 [[26, 40, 83], [49, 60, 57], [13, 89, 99]]
for _ in range(n):
    tmp = list(map(int, input().split()))
    colors.append(tmp)


for i in range(1, len(colors)):
    colors[i][0] = min(colors[i-1][1], colors[i-1][2]) + colors[i][0]
    colors[i][1] = min(colors[i-1][2], colors[i-1][0]) + colors[i][1]
    colors[i][2] = min(colors[i-1][0], colors[i-1][1]) + colors[i][2]

print(min(colors[n-1]))
    