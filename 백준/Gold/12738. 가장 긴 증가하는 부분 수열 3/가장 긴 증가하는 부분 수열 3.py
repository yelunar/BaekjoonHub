import sys 
# sys.stdin = open('input1.txt')
input = sys.stdin.readline

"""

"""
import bisect

n = int(input()) # 수열크기
arr = list(map(int, input().split()))
dp = [arr[0]]

for i in range(1, n):
    idx = bisect.bisect_left(dp, arr[i])
    if idx == len(dp):
        dp.append(arr[i])
    else:
        dp[idx] = arr[i]

print(len(dp))