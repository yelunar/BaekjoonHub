import sys
# sys.stdin = open('input2.txt')
input = sys.stdin.readline
sys.setrecursionlimit(100000)

"""
무게가 서로 다른 N 개의 물건이 있다. 각 물건은 1부터 N 까지 번호
일부 물건 쌍에 대해서 양팔 저울로 어떤 것이 무거운 것인지를 측정한 결과표있음

ans => 각 물건에 대해서 그 물건과의 비교 결과를 알 수 없는 물건의 개수를 출력
"""
n = int(input()) # 물건 개수
m = int(input()) # 측정된 물건 쌍 개수
graph = [[0] * (n+1) for _ in range(n+1)]
ans = 0

# 같은 지점 처리
for i in range(1, n+1):
    graph[i][i] = 0

# 그래프 정보 받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    # graph[b][a] = 1

# 플로이드워셜
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        # i에서 j로 갈 수 없고 j에서 i로 갈 수 없으면 무게를 비교할 수 없으므로 cnt를 증가
        if not graph[i][j] and not graph[j][i]:
            cnt += 1
    print(cnt-1) # 자기 자신을 빼줘야함