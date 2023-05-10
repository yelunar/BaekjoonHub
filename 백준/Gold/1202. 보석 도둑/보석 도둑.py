import sys
# sys.stdin = open('input2.txt')
input = sys.stdin.readline
sys.setrecursionlimit(100000)

"""
최대힙 사용
현재 bag 무게 이하의 훔칠 보석이 있다면(tmp), heappop으로 최대 가격의 보석을 빼서 ans에 갱신
"""
from heapq import heappop, heappush

n, k = map(int, input().split()) # 보석이 총 N개, 가방을 K개
jewels = [list(map(int, input().split())) for _ in range(n)] # 무게, 가격
bags = [int(input()) for _ in range(k)]
jewels.sort() # 1순위 무게 2순위 가격순으로 오름차순
bags.sort() # 무게순으로 오름차순
heap = []
ans = 0

tmp = []
for bag in bags: # 각 가방 무게에 대해서
    while jewels and jewels[0][0] <= bag: # 제일 가벼운 보석 들어갈 수 있는대로
        heappush(tmp, -jewels[0][1]) # 가격을 최대힙에 저장
        heappop(jewels)
    
    if tmp: # 작은 무게 보석 가격 다 저장했으면
        ans -= heappop(tmp) # 제일 높은 가격 더해줌

print(ans)