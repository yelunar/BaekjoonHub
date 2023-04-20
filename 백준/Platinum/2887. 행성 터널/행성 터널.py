import sys 
input = sys.stdin.readline

"""
터널로 연결할 때 드는 비용은 min(|xA-xB|, |yA-yB|, |zA-zB|)
mst -> 그래프에서 (사이클 없이) 연결하는 최단경로 
MST는 트리다!!!!!!!!!!
"""
# MST
def find_set(a): # 트리 루트노드 찾는 과정
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

####################################################

n = int(input()) # 행성개수
graph = [list(map(int, input().split())) + [i] for i in range(n)] 
parents = [i for i in range(n)]
arr = [] # [[0, 1, 0], [3, 4, 0], [0, 3, 1], [1, 3, 1], [1, 4, 1], [2, 3, 3], [2, 4, 3], [1, 2, 4], [0, 4, 8], [0, 2, 10]]

graph_x = sorted(graph, key = lambda x: x[0])
graph_y = sorted(graph, key = lambda x: x[1])
graph_z = sorted(graph, key = lambda x: x[2])
 
for i in range(n-1):
    distance_x = abs(graph_x[i][0] - graph_x[i+1][0])
    distance_y = abs(graph_y[i][1] - graph_y[i+1][1])
    distance_z = abs(graph_z[i][2] - graph_z[i+1][2])
    arr.append([graph_x[i][3], graph_x[i+1][3], distance_x])
    arr.append([graph_y[i][3], graph_y[i+1][3], distance_y])
    arr.append([graph_z[i][3], graph_z[i+1][3], distance_z])

arr.sort(key=lambda x:x[2]) # 거리 기준으로 정렬

ans = 0
for edge in arr:
    a, b, cost = edge
    if find_set(a) != find_set(b):
        union(a, b)
        ans += cost

print(ans)