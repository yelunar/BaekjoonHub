import sys
input = sys.stdin.readline
# sys.stdin = open('input3.txt')
# sys.setrecursionlimit(10**6)

"""
경사로는 높이가 항상 1
두개의 작은 길이가 연속해있어야함
"""

n, l = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0

# 가로
for i in range(n):
    before = arr[i][0]  # 초기 값 설정
    cnt = 1
    for j in range(1, n):
        if arr[i][j] == before:
            cnt += 1
            before = arr[i][j]
        elif arr[i][j] - before == 1 and cnt >= 0:
            if cnt >= l:
                cnt = 1
                before = arr[i][j]
            else:
                break
        elif arr[i][j] - before == -1 and cnt >= 0:
            cnt = 1 - l
            before = arr[i][j]
        else:
            break
    else:
        if cnt >= 0:
            ans += 1

# 세로
for j in range(n):
    before = arr[0][j]  # 초기 값 설정
    cnt = 1
    for i in range(1, n):
        if arr[i][j] == before:
            cnt += 1
            before = arr[i][j]
        elif arr[i][j] - before == 1 and cnt >= 0:
            if cnt >= l:
                cnt = 1
                before = arr[i][j]
            else:
                break
        elif arr[i][j] - before == -1 and cnt >= 0:
            cnt = 1 - l
            before = arr[i][j]
        else:
            break
    else:
        if cnt >= 0:
            ans += 1

print(ans)
