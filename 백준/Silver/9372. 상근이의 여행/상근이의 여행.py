import sys
# sys.stdin = open('input2.txt')
input = sys.stdin.readline
"""
 M개의 줄에 a와 b 쌍들이 입력된다. a와 b를 왕복하는 비행기가 있다는 것을 의미
"""

def tree(s):
    global ans
    visited[s] = True

    for i in arr[s]:
        if not visited[i]:
            ans += 1
            visited[i] = True
            tree(i)
    
T = int(input()) # tc

for tc in range(T):
    N, M = map(int, input().split()) #  국가의 수 N 비행기의 종류 M
    arr = [[] for _ in range(N+1)]
    
    for _ in range(M):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
    
    visited = [False] * (N+1)
    ans = 0
    
    tree(1)
    print(ans)