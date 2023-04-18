import sys
input = sys.stdin.readline
# sys.stdin = open('input3.txt')
sys.setrecursionlimit(10**6)

"""
<heap>
heapq.heappush(heap, item)
- item을 heap으로 push
heapq.heappop(heap)
- heap에서 가장 작은 항목을 pop
- heap이 비어있다면 IndexError 발생
heapq.heappushpop(heap, item)
- 힙에 item을 push한 다음, heap에서 가장 작은 항목을 pop
- heapq.heappush와 heapq.heappop을 이어서 호출하는 것과 동일한 결과이지만, 더 효율적으로 실행
heapq.heapify(x)
- 리스트 x를 heap으로 변환
"""
from heapq import heappush, heappop

def dijkstra(start):
    distance[start] = 0 # 출발노드를 선택하여 0 으로 초기화 (이유: 자기자신은 비용이 들지 않음)
    heap = []
    heappush(heap, [0, start])

    while heap:
        cost, start = heappop(heap) # heappop() 함수는 힙에서 최소값을 제거하고 반환
        if distance[start] < cost:
            continue
        for end, dist in arr[start]:
            ans = cost+ dist
            if distance[end] > ans:
                distance[end] = ans
                heappush(heap, [ans, end])

#------------------------------------------------------------------------------------

INF = int(1e9)
N = int(input()) # 도시의 개수 N
M = int(input()) # 버스의 개수 M

arr = [[] for _ in range(N + 1)]
distance = [INF for _ in range(N + 1)] #초기값을 최대값으로 지정


for i in range(M):
    start, end, cost = map(int, input().split())
    arr[start].append([end, cost]) # 노드를 그리면서 각 가중치도 같이 해줌
    
start, end = map(int, input().split()) # 우리가 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호

dijkstra(start)
print(distance[end])