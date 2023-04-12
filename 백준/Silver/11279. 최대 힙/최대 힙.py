import sys
input = sys.stdin.readline

from heapq import heappop, heappush

heap = []
n = int(input()) #연산개수
for _ in range(n):
    num = int(input())
    if num == 0:
        if len(heap)>0:  # 힙이 비어있는 경우에는 heappop을 수행하지 않도록 예외 처리
            print(-1*heappop(heap))
        else:
            print(0)
    else:
        heappush(heap, -num)
