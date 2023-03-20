import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

# N개의 자연수 중에서 M개를 고른 수열

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
lst = []

def backtracking(s):


    if len(lst) == m:
        print(*lst)
        return
    else:
        for i in range(n):
            if arr[i] < s:
                pass
            else:
                lst.append(arr[i])
                backtracking(arr[i])
                lst.pop()
        
backtracking(arr[0])