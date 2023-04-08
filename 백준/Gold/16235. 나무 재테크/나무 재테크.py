import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

"""

"""
from collections import deque

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 1, 0]

def spring_summer():
    for i in range(n):
        for j in range(n):
            num = len(trees[i][j]) # 땅에 있는 나무 개수

            for k in range(num): 
                # 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉사 (어린 나무부터)
                if arr[i][j] < trees[i][j][k]: 
                    for _ in range(k, num):
                        dead_trees[i][j].append(trees[i][j].pop())
                    break
                # 자신의 나이만큼 양분을 먹고, 나이가 1 증가
                else:
                    arr[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1

    # 죽은 나무마다 나이//2 값이 나무가 있던 칸에 양분으로 추가
    for i in range(n):
        for j in range(n):
            while dead_trees[i][j]:
                arr[i][j] += dead_trees[i][j].pop() // 2

       
def fall_winter():
    for i in range(n):
        for j in range(n):
            num = len(trees[i][j]) # 땅에 있는 나무 개수
            for k in range(num):
                #  번식하는 나무는 나이가 5의 배수이어야함
                if trees[i][j][k] % 5 == 0:
                    for l in range(8):
                        nx = i + dx[l]
                        ny = j + dy[l]
                        # 인접한 8개의 칸에 나이가 1인 나무가 생김 땅 범위 벗어나면 나무 안생김
                        if 0<= nx < n and 0<= ny < n:
                            trees[nx][ny].appendleft(1)
           
            #  땅을 돌아다니면서 땅에 양분을 추가
            arr[i][j] += add[i][j] 


#------------------------------------------------------------------

n, m, k = map(int, input().split())
arr = [[5]*n for _ in range(n)]
add = [list(map(int, input().split())) for _ in range(n)]
trees = [[deque() for _ in range(n)] for _ in range(n)] # 나무들의 정보 저장 3차원 리스트
dead_trees = [[list() for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y, age = map(int, input().split())
    trees[x-1][y-1].append(age)

for _ in range(k):
    spring_summer()
    fall_winter()

# ans -> K년이 지난 후 상도의 땅에 살아있는 나무의 개수?
ans = 0
for i in range(n):
    for j in range(n):
        ans += len(trees[i][j])

print(ans)