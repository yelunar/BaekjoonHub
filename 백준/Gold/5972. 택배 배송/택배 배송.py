import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10000)
"""
N (1 <= N <= 50,000) 개의 헛간과, 소들의 길인 M (1 <= M <= 50,000) 개의 양방향 길
각각의 길은 C_i (0 <= C_i <= 1,000) 마리의 소
 소들의 길은 두 개의 떨어진 헛간인 A_i 와 B_i (1 <= A_i <= N; 1 <= B_i <= N; A_i != B_i)를 이음

ans =>  지나가는 길에 소를 만나면 줘야할 여물의 비용이 주어질 때 최소 여물은 얼마
"""
from heapq import heappush, heappop

def dijkstra(start):

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
n, m = map(int, input().split()) # 헛간 , 길 개수
graph = [[] for _ in range(n+1)]
distance = [INF for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

ans = INF
dijkstra(1)
print(distance[n])