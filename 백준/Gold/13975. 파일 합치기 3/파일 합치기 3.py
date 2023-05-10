import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10000)

"""
ans => 종적인 한 개의 파일을 완성하는데 필요한 비용의 총 합

파일 중 제일 작은 두개 뽑아서 -> 합치고 -> 다시 넣음
"""
from heapq import heappop, heappush

T = int(input())  # test case

for _ in range(T):
    K = int(input()) # 소설의 장의 수
    arr = list(map(int, input().split()))
    ans = 0
    heap = []

    for i in arr:
        heappush(heap, i)

    while len(heap) > 1:
        a = heappop(heap)
        b = heappop(heap)
        ans += (a + b)
        heappush(heap, a+b)
    
    print(ans)
