import sys
input = sys.stdin.readline
# sys.stdin = open('input3.txt')
# sys.setrecursionlimit(10**6)

"""
 
"""
# 특정 원소가 속한 집합을 찾기
def find(x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

########################################################################


n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]
parent = [_ for _ in range(n+1)]

# 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges = []
result = 0

# 모든 노드에 대해 연결 정보를 저장
for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:
            edges.append((0, i+1, j+1))
        else:
            if ord('a') <= ord(arr[i][j]) <= ord('z'):
                edges.append((ord(arr[i][j])-ord('a')+1, i+1, j+1))
                result += ord(arr[i][j])-ord('a')+1

            elif ord('A') <= ord(arr[i][j]) <= ord('Z'):
                edges.append((ord(arr[i][j])-ord('A')+27, i+1, j+1))
                result += ord(arr[i][j])-ord('A')+27

edges.sort(key=lambda x: x[0])  # 간선들을 가중치 기준(오름차순)으로 정렬

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    if cost == 0:
        continue
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find(a) != find(b):
        union(a, b)
        result -= cost

# 모든 노드의 루트 노드를 찾아서 중복되지 않은 값들만 추가
ans = set()
for i in range(1, n+1):
    if find(i) not in ans:
        ans.add(find(i))

if len(ans) == 1:  # 모든 컴퓨터가 연결되어 있으면
    print(result)
else:
    print(-1)
