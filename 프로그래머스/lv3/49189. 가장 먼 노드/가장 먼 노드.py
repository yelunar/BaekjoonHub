from collections import deque

def solution(n, edge):
    answer = 0
    arr = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    
    for v1, v2 in edge:
        arr[v1].append(v2)
        arr[v2].append(v1)
    
    visited[1] = 1
    queue = deque()
    queue.append(1)
    
    while queue:
        now = queue.popleft()
        for i in arr[now]:
            if not visited[i]:
                visited[i] = visited[now] + 1
                queue.append(i)
                
    max_one = max(visited)
    answer = visited.count(max_one)
    
    return answer