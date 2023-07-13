import sys
input = sys.stdin.readline
# sys.stdin = open('input3.txt')
# sys.setrecursionlimit(10**6)

"""

"""

n = int(input())  # 저울추의 개수
arr = list(map(int, input().split()))
arr.sort()  # [1, 1, 2, 3, 6, 7, 30]

num = 1

for i in arr:
    if num < i:
        break
    num += i

print(num)