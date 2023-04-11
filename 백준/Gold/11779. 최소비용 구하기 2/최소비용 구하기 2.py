import sys
# sys.stdin = open('input2.txt')
input = sys.stdin.readline
sys.setrecursionlimit(100000)

"""
(1) 도착 도시까지 가는데 드는 최소 비용을 출력
(2) 최소 비용을 갖는 경로에 포함되어있는 도시의 개수를 출력 (출발 도시와 도착 도시도 포함)
(3) 최소 비용을 갖는 경로를 방문하는 도시 순서대로 출력
"""
from heapq import heappop, heappush

def dijkstra(start):
    heap = []
    distance[start] = 0
    heappush(heap, [0, start])

    while heap:
        cost, start = heappop(heap)

        if distance[start] < cost:
            continue
        for go, expense in arr[start]:
            ans = cost + expense
            if ans < distance[go]:
                distance[go] = ans
                prev_node[go] = start
                heappush(heap, [ans, go])

#-----------------------------------------------------------------------------

INF = int(1e9)
n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)] 
# [[], [[2, 2], [3, 3], [4, 1], [5, 10]], [[4, 2]], [[4, 1], [5, 1]], [[5, 3]], []]
distance = [INF for _ in range(n+1)] 
prev_node = [0] * (n+1)

for _ in range(m):
    start, end, cost = map(int, input().split())
    arr[start].append([end, cost])

start, end = map(int, input().split())

dijkstra(start)
print(distance[end])

path = [end]
now = end

while now != start:
    now = prev_node[now]
    path.append(now)
path.reverse()

print(len(path))
print(*path)