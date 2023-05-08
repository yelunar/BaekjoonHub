import sys
# sys.stdin = open('input2.txt')
input = sys.stdin.readline
sys.setrecursionlimit(100000)

"""
N개의 숫자로 구분된 각각의 마을에 한 명의 학생이 살고 있다.
N명의 학생이 X (1 ≤ X ≤ N)번 마을에 모여서 파티
이 마을 사이에는 총 M개의 단방향 도로들이 있고 i번째 길을 지나는데 Ti(1 ≤ Ti ≤ 100)의 시간을 소비
이 도로들은 단방향이기 때문에 아마 그들이 오고 가는 길이 다를지도 모른다. 

ans => N명의 학생들 중 오고 가는데 가장 많은 시간을 소비하는 학생은 누구일지 
"""
from heapq import heappush, heappop

def dijkstra(start): # 다익스트라 기본 식
    distance = [INF for _ in range(n+1)]
    distance[start] = 0 # 출발노드 선택하여 0으로 초기화
    heap = []
    heappush(heap, [0, start])

    while heap:
        cost, start = heappop(heap)
        if distance[start] < cost:
            continue
        for end, dist in graph[start]:
            ans = cost+ dist
            if distance[end] > ans:
                distance[end] = ans
                heappush(heap, [ans, end])

    return distance

################################################################################


INF = int(1e9)
n, m, x= map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b,c])

ans = 0
for i in range(1, n+1):
    if i != x:
        ans = max(dijkstra(i)[x]+dijkstra(x)[i], ans)
print(ans)