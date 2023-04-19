import sys
input = sys.stdin.readline
# sys.stdin = open('input3.txt')
sys.setrecursionlimit(10**6)

"""
ANS => 도로 개수가 최소일 때, 모든 도로의 시간의 합을 출력한다. 불가능한 경우에는 -1을 출력

<과정>
1. 입력을 받고, road 정의 ( i에서 j로 가는 도로가 있으면 True )
2. 플로이드워셜
    - i, j, k가 모두 다른 값이고 arr[i][j] == arr[i][k]+arr[k][j] 이면 다른 도시를 거쳐 왔다는 뜻 : 도로 False
    - i, j, k가 모두 다른 값이고 arr[i][j] > arr[i][k]+arr[k][j] 이면 최솟값이 아님 : result = -1
3. result가 0 그대로이면
    - 각 존재하는 도로의 가중치를 더해줌
4. result 출력
"""

n = int(input()) # 도시개수
graph = [list(map(int, input().split())) for _ in range(n)] # 도시 사이에 이동하는데 필요한 시간
road = [[True]*n for _ in range(n)]
result = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j and k != j and i != k:
                if graph[i][j] == graph[i][k] + graph[k][j]: # 다른 도시를 거쳐 왔다는 뜻 : 도로 False
                    road[i][j] = False
                elif graph[i][j] > graph[i][k] + graph[k][j]: # 최솟값이 아님 : result = -1
                    result = -1
if not result:
    for i in range(n):
        for j in range(i, n):
            if road[i][j]:
                result += graph[i][j]
print(result)