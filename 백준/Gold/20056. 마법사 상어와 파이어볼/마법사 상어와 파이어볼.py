import sys 
# sys.stdin = open('input1.txt')
input = sys.stdin.readline

"""
i번 파이어볼의 위치는 (ri, ci), 질량은 mi이고, 방향은 di, 속력은 si
위치 (r, c)는 r행 c열
1번 행은 N번과 연결되어 있고, 1번 열은 N번 열과 연결되어 있다.
0 0 5 2 2
1 3 7 1 6
"""
from collections import deque

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

n, m, k = map(int, input().split()) # N×N인 격자에 파이어볼 M개 K번 명령
fireballs = []
arr = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    ri, ci, mi, si, di = map(int, input().split())
    fireballs.append([ri-1, ci-1, mi, si, di])

for _ in range(k):

    while fireballs:
        ri, ci, mi, si, di = fireballs.pop() # x, y, 질량, 속력, 방향
        new_ri = (ri + dx[di]*si) % n
        new_ci = (ci + dy[di]*si) % n
        arr[new_ri][new_ci].append([mi, si, di])

    for i in range(n):
        for j in range(n):
            
            if len(arr[i][j]) >= 2: # 2개 이상인지 확인

                # 질량합, 속력합, 짝수합, 홀수합, 파이어볼개수
                sum_mi, sum_si, check_even, check_odd, cnt = 0, 0, 0, 0, len(arr[i][j])
                while arr[i][j]:
                    mi, si, di = arr[i][j].pop()
                    sum_mi += mi
                    sum_si += si
                    if di % 2: #홀수
                        check_odd += 1
                    else:
                        check_even += 1
                if check_even == cnt or check_odd == cnt:
                    dir = [0, 2, 4, 6]
                else:
                    dir = [1, 3, 5, 7]
                if sum_mi //5: # 소멸 안하면
                    for d in dir:
                        fireballs.append([i, j, sum_mi//5, sum_si//cnt, d])
                
            if len(arr[i][j]) == 1: # 파이어볼 하나 있으면
                fireballs.append([i, j] + arr[i][j].pop())


print(sum([i[2] for i in fireballs]))