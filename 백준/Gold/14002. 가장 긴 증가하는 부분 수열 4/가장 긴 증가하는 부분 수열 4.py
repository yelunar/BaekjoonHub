import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10000)

"""
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성
"""
n = int(input()) # 수열길이
arr = list(map(int, input().split())) # 10 20 10 30 20 50
dp = [1] * (n+1)

for i in range(len(arr)):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)
num = max(dp)
print(num)

ans = []
for i in range(n-1, -1, -1):
    if dp[i] == num:
        ans.append(arr[i])
        num -= 1
ans.reverse()
for i in ans:
    print(i, end=' ')