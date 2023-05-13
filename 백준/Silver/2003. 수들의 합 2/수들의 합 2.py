import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10000)

"""

"""
n, m = map(int, input().split())
arr = list(map(int, input().split()))
start, end = 0, 1
cnt = 0

while start <= n and end <= n:
    sum_nums = arr[start:end]
    result = sum(sum_nums)

    if result == m:
        cnt += 1
        end += 1
        start += 1
    elif result < m:
        end += 1
    else:
        start += 1
print(cnt)