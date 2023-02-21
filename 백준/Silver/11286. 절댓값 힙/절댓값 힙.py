# 절댓값 힙
# 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거
# 절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 
# 그 값을 배열에서 제거

import sys
import heapq

heap = []

N = int(sys.stdin.readline()) # 연산 개수

for _ in range(N):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, (abs(num), num))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)