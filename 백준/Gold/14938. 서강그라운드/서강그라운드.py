import sys
input = sys.stdin.readline
# sys.stdin = open("input1.txt")
sys.setrecursionlimit(1000000)

"""
플로이드 워셜 -> 모든 지점에서 모든 지점까지의 최단 거리를 구함

(1) 플로이드 워셜 알고리즘 만들기
(2) 시작지점에서 도달지점까지의 거리가 수색 범위 내이면 아이템 회수하기
(3) 2번을 반복 후 예은이가 얻을 수 있는 최대 아이템 개수를 출력
"""

INF = int(1e9)
n, m, r = map(int, input().split()) # 지역, 수색범위, 길의 개수
item = list(map(int, input().split())) # 아이템 개수
arr = [[INF] * (n+1) for _ in range(n+1)]
ans = 0

# 같은 지점 0처리
for i in range(1, n+1):
    arr[i][i] = 0

# 그래프 정보
for _ in range(r):
    a, b, c = map(int, input().split()) # 지역번호 a,b 길의 길이
    arr[a][b] = c
    arr[b][a] = c

# 플로이드 워셜
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if arr[i][j] <= m:
            cnt += item[j-1]

    ans = max(ans, cnt) # 최대값 반환

print(ans)