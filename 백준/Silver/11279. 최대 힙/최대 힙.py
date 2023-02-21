import sys
import heapq

heap = []

N = int(input()) # 연산 개수

for _ in range(N):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, -num)
    else:
        try:
            print(-1*heapq.heappop(heap))
        except:
            print(0)