import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
lst = []

def backtracking(s):
    if len(lst) == m:
        print(*lst)
        return
    else:
        for i in arr:
            lst.append(i)
            backtracking(i)
            lst.pop()

backtracking(arr[0])