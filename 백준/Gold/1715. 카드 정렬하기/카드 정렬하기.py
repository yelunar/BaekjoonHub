from heapq import heappop, heappush
import sys
# sys.stdin = open('input2.txt')
input = sys.stdin.readline
sys.setrecursionlimit(100000)

"""

"""
n = int(input())
arr = [int(input()) for _ in range(n)]
heap = []
cnt = 0
for i in arr:
    heappush(heap, i)

while len(heap) > 1:
    a = heappop(heap)
    b = heappop(heap)
    cnt += (a+b)
    heappush(heap, a+b)

print(cnt)