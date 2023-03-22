import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations

"""
 빈 칸, 치킨집, 집 
 도시의 칸은 (r, c)와 같은 형태
r과 c는 1부터 시작

0은 빈 칸, 1은 집, 2는 치킨집

가장 수익을 많이 낼 수 있는  치킨집의 개수는 최대 M
어떻게 고르면, 도시의 치킨 거리가 가장 작게 될지

ans를 처음값으로 가정한후에 ans보다 크면 백트래킹
site는 ... 조합같이 .. 
"""

# def DFS(x, y):
#     tmp = 0
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 1:
#                 tmp += abs(x-i) + abs(y-j)
    
#     lst.append(tmp)
#     return

N, M = map(int, input().split()) # M-> 치킨집 개수
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0 # 치킨 거리 넣는 리스트
lst = [] # 2 좌표 모은 리스트 [[0, 1], [3, 0], [4, 0], [4, 1], [4, 4]]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            lst.append([i,j])

answer = [] # 도시치킨거리 모아둔 리스트
for i in combinations(range(len(lst)), M): # 2 좌표 정해졌을 때

    result = 0
    for x in range(N):
        for y in range(N):
            tmp = 0
            tlst = [] # 한 지점에서 각 치킨집까지 거리 모음집
            if arr[x][y] == 1:
                for z in i:
                    tmp = abs(lst[z][0] - x) + abs(lst[z][1] - y)              
                    tlst.append(tmp)
                result += min(tlst)
    answer.append(result)

print(min(answer))