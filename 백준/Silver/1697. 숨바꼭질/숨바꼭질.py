import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10000)

"""
하.. 변수명 겹치는거 써서 많이 틀림 ;;
"""
from collections import deque

n, k = map(int, input().split())
visited = [0 for _ in range(100001)]

def bfs():
    queue = deque()
    queue.append(n)
    visited[n] = 1  # 이거 안해줘서 이지경이 났다.. 

    while queue:
        s = queue.popleft()
        if s == k:
            print(visited[s]-1)
            break   
        
        for ns in (s-1, s+1, s*2):
            if 0<= ns < 100001 and not visited[ns]:
                visited[ns] = visited[s] + 1
                queue.append(ns)
    
bfs()