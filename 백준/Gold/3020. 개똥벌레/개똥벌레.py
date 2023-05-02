import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10000)

"""
동굴의 길이는 N미터이고, 높이는 H미터
첫 번째 장애물은 항상 석순이고, 그 다음에는 종유석과 석순이 번갈아가면서 등장

ans => 개똥벌레가 파괴해야 하는 장애물의 최솟값과 그러한 구간의 수
"""

from bisect import bisect_left # target값이 list에 삽입될 위치를 return

n, h = map(int, input().split()) # 동굴의 길이는 N미터이고, 높이는 H미터
up = [] # 종유석
down = [] # 석순
for i in range(n):
    if i%2:
        up.append(int(input()))
    else:
        down.append(int(input()))
up.sort() # [1, 3, 5] # 높이 순으로 정렬
down.sort() # [1, 3, 5]

cnt = 0
mini = 1e9
for height in range(1, h+1):
    up_item , down_item = bisect_left(up, (h+1)-height), bisect_left(down, height)
    # 높이가 height 인것들의 인덱스 추출
    total = n - (up_item+down_item)

    if total < mini:
        mini = total
        cnt = 1
    elif total == mini:
        cnt += 1

print(mini, cnt)
