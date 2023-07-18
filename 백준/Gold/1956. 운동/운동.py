import sys
input = sys.stdin.readline
# sys.stdin = open('input3.txt')

"""
최소 사이클의 도로 길이의 합을 출력
"""
INF = sys.maxsize
v, e = map(int, input().split())
arr = [[INF] * (v+1) for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    arr[a][b] = c

# 플로이드 워셜
for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            arr[i][j] = min(arr[i][j], arr[i][k]+arr[k][j])

ans = INF  # 정답을 최대값으로 설정해둔다
for i in range(1, v+1):
    ans = min(ans, arr[i][i])

if ans == INF:
    ans = -1

print(ans)