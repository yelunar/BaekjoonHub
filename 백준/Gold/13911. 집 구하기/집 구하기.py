import sys
input = sys.stdin.readline
# sys.stdin = open('input3.txt')
sys.setrecursionlimit(10**6)

"""
맥세권 : 맥세권인 집은 맥도날드와 집 사이의 최단거리가 x이하인 집이다.
스세권 : 스세권인 집은 스타벅스와 집 사이의 최단거리가 y이하인 집이다.
맥세권과 스세권을 만족하는 집 중 최단거리의 합이 최소인 집

"""
import heapq

def dijkstra(distance, heap, limit):

    while heap:
        cost, start = heapq.heappop(heap) # heappop() 함수는 힙에서 최소값을 제거하고 반환
        if distance[start] < cost:
            continue
        for next in graph[start]:
            ans = distance[start]+ next[1]
            if ans > limit:
                continue
            if distance[next[0]] > ans:
                distance[next[0]] = ans
                heapq.heappush(heap, [ans, next[0]])


######################################################################

INF = int(1e9)

v, e = map(int, input().split()) # 정점개수, 도로개수
graph = [[] for _ in range(v+1)] # 도로 가중치
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

M,x = map(int,input().split()) # 맥날 수, 맥날까지 거리 x이하
mac = list(map(int,input().split())) # 맥날 노드번호

S,y = map(int,input().split()) # 스벅 수, 스벅까지 거리 y이하
star = list(map(int,input().split())) #스벅 노드번호
total = mac + star
mini = sys.maxsize

distance_mac = [INF]*(v+1) #초기값을 최대값으로 지정
distance_star = [INF]*(v+1) #초기값을 최대값으로 지정
mac_heap, star_heap = [],[]

for i in mac:
    distance_mac[i] = 0 # 초기값 초기화
    heapq.heappush(mac_heap, [0, i])

for i in star:
    distance_star[i] = 0
    heapq.heappush(star_heap,[0, i])

dijkstra(distance_mac, mac_heap, x)
dijkstra(distance_star, star_heap, y)

for i in range(1, v+1):
    if i not in total:
        mini = min(mini, distance_mac[i]+distance_star[i])

if mini >= INF:
    mini = -1

print(mini)