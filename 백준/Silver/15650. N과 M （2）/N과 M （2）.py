import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline
from itertools import permutations

n, m = map(int, input().split())
arr = []
# arr.append(permutations(range(3), 2))


for i in permutations(range(1, n+1), m):
    a = sorted(set(i))
    arr.append(a)

ans = []

for i in arr:
    if i not in ans:
        ans.append(i)

for i in ans:
    # k = ''.join(i)
    print(*i)