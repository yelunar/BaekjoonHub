import sys
# sys.stdin = open('input2.txt')
input = sys.stdin.readline
# sys.setrecursionlimit(100000)

"""
 
"""
# MST 대표 함수 find_set 과 union
def find_set(a):
    if a == parents[a]:
        return a
    else:
        b = find_set(parents[a])
        parents[a] = b
        return b

def union(a, b):
    a = find_set(a)
    b = find_set(b)
    if a != b:
        parents[b] = a

#############################################################################

n, m = map(int, input().split()) # 학교의 수 N와 학교를 연결하는 도로의 개수 M
wms = input().split() # 대학교 성별들
edges = [] 
parents = [i for i in range(n+1)] # parents : 각 정점의 부모 원소 (초기 설정: 모두 자기 자신)
ans, distance = 0, 0

for _ in range(m):
    u, v, cost = map(int, input().split())
    edges.append((u, v, cost))
edges.sort(key=lambda x : x[2]) # 간선을 비용순으로 오름차순 정렬

for edge in edges:
    u, v, cost = edge
    if find_set(u) != find_set(v) and wms[v-1] != wms[u-1]:   # 해당 간선이 사이클을 만들지 않는다면
        union(u, v)# union 연산을 수행한다. (b의 대표 원소가 a의 대표 원소를 가리키게 한다.)
        ans += cost
        distance += 1

if distance != n-1:
    ans = -1
print(ans)
