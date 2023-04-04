import sys
# sys.stdin = open('input2.txt')
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

#목적지까지 최단거리(시간)를 구하는 문제이기 때문에 BFS
"""
<0 - 1 bfs 탐색>
- 동생의 위치에 도달했다면 리턴하고 도달하지 못했다면 이동
- 이동은 3가지 방법을 반복문을 통해 수행
- 이동하는 곳이 범위 내에 있고 이동하지 않은 곳이라면 이동
- 순간이동이라면 이전에 초로 갱신하고 appendleft()로 탐색
- 순간이동이 아니라면 이전에 초에 +1 해주고 append()로 탐색

=>  큐에 삽입하는 위치를 달리해서 위의 '우선순위' 기능을 대신한다. 
이때 가중치가 0이면 우선순위가 높으므로 큐의 앞에, 1이면 큐의 뒤에 삽입
"""

from collections import deque

n, k = map(int, input().split()) # 현재수빈이n 동생위치k
queue = deque()
queue.append(n)
visited = [-1 for _ in range(100001)]
visited[n] = 0

while queue:
    s = queue.popleft()
    if s == k: # 동생의 위치에 도달했다면 리턴
        print(visited[s])
        break
    
    if 0<= s-1 < 100001 and visited[s-1] == -1: # 이동하는 곳이 범위 내에 있고 이동하지 않았다면 이동
        visited[s-1] = visited[s] + 1
        queue.append(s-1)

    if 0<= s*2 < 100001 and visited[s*2] == -1:  # 순간이동이라면
        visited[s*2] = visited[s] # 0초 갱신
        queue.appendleft(s*2) # 더 높은 우선순위 가지라고 앞에 넣음

    if 0<= s+1 < 100001 and visited[s+1] == -1: # 이동하는 곳이 범위 내에 있고 이동하지 않았다면 이동
        visited[s+1] = visited[s] + 1
        queue.append(s+1)