# 모든 수는 자신의 한 칸 위에 있는 수보다 크다
# N번째 큰 수 찾기

import sys
import heapq

N = int(sys.stdin.readline()) # 줄 개수
heap = []

for _ in range(N):
    numbers = map(int, sys.stdin.readline().split())
    for num in numbers:
        if len(heap) < N:
            heapq.heappush(heap, num)
        else:
            if heap[0] < num:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

print(heap[0])
