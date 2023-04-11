import sys
input = sys.stdin.readline

"""
<조건>
한 학기에 들을 수 있는 과목 수에는 제한이 없다.
모든 과목은 매 학기 항상 개설된다.
ans => 1번 과목부터 N번 과목까지 차례대로 최소 몇 학기에 이수할 수 있는지를 한 줄에 공백으로 구분하여 출력

<위상정렬>
위상 정렬: 사이클이 없는 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것

진입차수(Indegree): 특정한 노드로 들어오는 간선의 개수
진출차수(Outdegree): 특정한 노드에서 나가는 간선의 개수

- 큐를 이용하는 위상 정렬 알고리즘의 동작 과정은 다음과 같다
    1. 진입차수가 0인 모든 노드를 큐에 넣는다
    2. 큐가 빌 때까지 다음의 과정을 반복한다
        큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거한다
        새롭게 진입차수가 0이 된 노드를 큐에 넣는다
    => 결과적으로 각 노드가 큐에 들어온 순서가 위상 정렬을 수행한 결과와 같다
"""

n, m = map(int, input().split()) # n과목수 m선수조건수
graph = [1] * (n+1) # 결과 반환 리스트
arr = [[] for _ in range(n+1)] # 조건 입력 리스트 [[], [2, 3], [5], [], [5], [], []]

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)

for i in range(1, n+1):
    for j in arr[i]:
        graph[j] = max(graph[j], graph[i]+1)

print(*graph[1:])

"""
<위상 정렬 알고리즘 (Python)>

from collections import deque

# 노드의 개수와 간선의 개수를 입력 받기
v, e = map(int, input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(v + 1)]

# 방향 그래프의 모든 간선 정보를 입력 받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # 정점 A에서 B로 이동 가능
    # 진입 차수를 1 증가
    indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 위상 정렬을 수행한 결과 출력
    for i in result:
        print(i, end=' ')

topology_sort()

"""