import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

n, m = map(int, input().split())
lst = []

def backtracking(s):
    if len(lst) == m:
        print(*lst)
        return
    else:
        for i in range(1, n+1):
            lst.append(i)
            backtracking(i)
            lst.pop()

backtracking(1)