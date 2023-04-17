import sys
# sys.stdin = open('input2.txt')
input = sys.stdin.readline
# sys.setrecursionlimit(100000)

"""
< 최소 신장 트리 (MST: Minimum Spanning Tree) >
 무방향 그래프에서 간선들의 가중치 합이 최소인 신장 트리
 트리의 일종이므로, 사이클이 존재하지 않는다.
 그래프의 정점이 n개라면, n - 1개의 간선을 가진다.

MST

1. 가중치 낮은거 부터 정렬
2. 싸이클 생기는지 확인
3. 없으면 가중치 낮은 애들 중 노드 끼리 전부 연결
4. 가중치 합 
 
"""

def union_find(x):
    # x의 대표원소를 찾아서 리턴한다.
    while x != parents[x]:
        x = parents[x]
    return x

################################################################

v, e = map(int, input().split()) # 정점의 개수 V 간선의 개수 E
graph = []

for _ in range(e):
    x, y, value = map(int, input().split())
    graph.append((x, y, value))

# 간선을 비용순으로 오름차순 정렬(구하고자 하는 애를 기준으로 정렬하면 됨)
graph.sort(key=lambda x: x[2])
 
# parents : 각 정점의 부모 원소 (초기 설정: 모두 자기 자신)
# cnt : 찾은 간선의 개수
parents = [x for x in range(v+1)]
distance, cnt = 0, 0

for a, b, value in graph:
    # 해당 간선이 사이클을 만들지 않는다면
    if union_find(a) != union_find(b):
        # union 연산을 수행한다. (b의 대표 원소가 a의 대표 원소를 가리키게 한다.)
        parents[union_find(b)] = union_find(a)
        distance += value
        cnt += 1

        # N - 1개의 간선을 모두 찾은 경우, 탐색을 종료한다.
        if cnt >= v - 1:
            break

print(distance)
