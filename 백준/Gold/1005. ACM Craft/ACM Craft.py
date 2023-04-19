import sys 
# sys.stdin = open('input3.txt')
input = sys.stdin.readline

"""


"""
from collections import deque

for _ in range(int(input())):
    n, k = map(int, input().split()) # 건물개수 n 건설순서규칙 총 개수 k
    time = [0] + list(map(int, input().split())) # [0, 10, 1, 100, 10]
    result = [0] * (n+1) # 결과 반환 리스트
    arr = [[] for _ in range(n+1)] # 조건 입력 리스트 [[], [2, 3], [4], [4], []]
    indegree = [0] * (n + 1) # 모든 노드에 대한 진입차수는 0으로 초기화

    for _ in range(k):
        a, b = map(int, input().split())
        arr[a].append(b) # X를 지은 다음에 건물 Y를 짓는 것이 가능
        indegree[b] += 1 # 진입 차수를 1 증가
   
    w = int(input()) # 승리하기 위해 건설해야 할 건물의 번호
    
    # 위상정렬 ----------------------------------------------------------------------
    queue = deque()
    for i in range(1, n+1): # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
        if indegree[i] == 0:
            queue.append(i)
            result[i] = time[i]
    
    while queue:
        now = queue.popleft()
        if now == w:
            break

        for i in arr[now]:
            result[i] = max(result[i], result[now] + time[i])

            if indegree[i] == 1:
                queue.append(i)
            indegree[i] -= 1

    print(result[w])