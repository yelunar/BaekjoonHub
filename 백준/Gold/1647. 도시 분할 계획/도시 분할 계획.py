import sys
# sys.stdin = open('input2.txt')
input = sys.stdin.readline
# sys.setrecursionlimit(100000)

"""
 문제를 잘보면 한 마을안에는 최소 1개의 집이 존재해야한다고 한다. 
 반대로 생각해보면 집을 1개만 남겨도 된다는 뜻이다. 
 따라서 크루스칼로 최소신장 트리를 만들면서
 마지막에 연결되는 길만 없애주면 무조건 마을 2개를 만들 수 있으며 최소길이로 만들 수 있다.
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
    if a < b: # 양방향이니까 이 조건 들어간다
        parents[b] = a
    else:
        parents[a] = b
#############################################################################

n, m = map(int, input().split()) # 집의 개수 N, 길의 개수 M
edges = [] 
parents = [i for i in range(n+1)] # parents : 각 정점의 부모 원소 (초기 설정: 모두 자기 자신)
ans = 0
end = 0

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((a, b, cost))
edges.sort(key=lambda x : x[2]) # 간선을 비용순으로 오름차순 정렬

for edge in edges:
    u, v, cost = edge
    if find_set(u) != find_set(v):   # 해당 간선이 사이클을 만들지 않는다면
        union(u, v)# union 연산을 수행한다. (b의 대표 원소가 a의 대표 원소를 가리키게 한다.)
        ans += cost
        end = cost # 마지막 비용이 저장될때까지 계속 저장 값 갱신해줌
print(ans- end)
