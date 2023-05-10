from heapq import heappop, heappush
import sys
# sys.stdin = open('input2.txt')
input = sys.stdin.readline
sys.setrecursionlimit(100000)

"""

"""
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()
heap = []
cnt = 0

for study in arr:
    while heap and heap[0] <= study[0]:
        heappop(heap)
    heappush(heap, study[1])
    cnt = max(cnt, len(heap))
print(cnt)
