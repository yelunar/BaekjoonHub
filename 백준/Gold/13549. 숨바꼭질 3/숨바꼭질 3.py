import sys
# sys.stdin = open('input2.txt')
input = sys.stdin.readline
sys.setrecursionlimit(100000)

"""
X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동
순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동
ans => 수빈이가 동생을 찾는 가장 빠른 시간을 출력

목적지까지의 "최단경로(시간)" 이므로 BFS!
---------------------------------------------------------------

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

n, k = map(int, input().split()) # 수빈이가 있는 위치 N과 동생이 있는 위치 K
queue = deque()
queue.append(n) # 현재 수빈이 위치

visited = [-1 for _ in range(100001)]
visited[n] = 0

while queue:
    start = queue.popleft()
    if start == k : # 동생 위치에 도달했으면 리턴
        print(visited[start])
        break
    
    if 0 <= start-1 < 100001 and visited[start-1] == -1: # 이동하는 곳이 범위 내에 있고 이동하지 않았다면 이동
        visited[start-1] = visited[start] + 1
        queue.append(start -1)

    if 0 <= start * 2 < 100001 and visited[start*2] == -1: # 순간이동 이면
        visited[start*2] = visited[start] # 0초 갱신
        queue.appendleft(start*2) # 더 높은 우선순위 가지라고 앞에 넣음
    
    if 0 <= start+1 < 100001 and visited[start+1] == -1: # # 이동하는 곳이 범위 내에 있고 이동하지 않았다면 이동
        visited[start+1] = visited[start] + 1
        queue.append(start+1)