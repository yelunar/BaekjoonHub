import sys

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
sort_arr = sorted(arr)

ans = [0] * n

for i in range(n):
  idx = sort_arr.index(arr[i])
  ans[i] = idx
  sort_arr[idx] = -1

print(*ans)