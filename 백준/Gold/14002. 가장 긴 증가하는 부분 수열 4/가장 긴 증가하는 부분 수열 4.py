import sys
# sys.stdin = open('input2.txt')
input = sys.stdin.readline
sys.setrecursionlimit(100000)

"""
"""
n = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

x = []
idx = max(dp)
for i in range(n-1, -1, -1):
    if dp[i] == idx:
        x.append(arr[i])
        idx -= 1
x.reverse()
print(*x)
