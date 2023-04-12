import sys
input = sys.stdin.readline
# sys.stdin = open('input3.txt')
sys.setrecursionlimit(10**6)

"""


"""
from heapq import heappush, heappop

def dijkstra(start):
    distance = [INF for _ in range(n + 1)] #초기값을 최대값으로 지정

    distance[start] = 0 # 출발노드를 선택하여 0 으로 초기화 (이유: 자기자신은 비용이 들지 않음)
    heap = []
    heappush(heap, [0, start]) # [[0, 1]]

    while heap:
        cost, start = heappop(heap) # heappop() 함수는 힙에서 최소값을 제거하고 반환
        if distance[start] < cost:
            continue
        for end, dist in graph[start]:
            ans = cost+ dist
            if distance[end] > ans:
                distance[end] = ans
       
                heappush(heap, [ans, end])
    
    return distance
#------------------------------------------------------------------------------------

INF = int(1e9)
n, e = map(int, input().split()) # 정점의 개수 N과 간선의 개수 E
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2 = map(int, input().split()) # 2 3

# 출발점이 각각 1, v1, v2일 때의 최단 거리 배열
original_distance = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

v1_path = original_distance[v1] + v1_distance[v2] + v2_distance[n]
v2_path = original_distance[v2] + v2_distance[v1] + v1_distance[n]

result = min(v1_path, v2_path)
print(result if result < INF else -1)